package main

import (
	"encoding/json"
	"log"
	"net/http"
	"os"
	"strconv"
	"strings"
	"time"

	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
	"elden-ring-api/models"
)

var (
	weapons   []models.Weapon
	categories []models.Category
)

func main() {
	// Load environment variables
	if err := godotenv.Load(); err != nil {
		log.Println("No .env file found, using default configuration")
	}

	// Load data
	if err := loadData(); err != nil {
		log.Fatal("Failed to load data:", err)
	}

	// Set Gin mode
	if os.Getenv("GIN_MODE") == "release" {
		gin.SetMode(gin.ReleaseMode)
	}

	// Create router
	r := gin.Default()

	// Configure CORS
	config := cors.DefaultConfig()
	config.AllowAllOrigins = true
	config.AllowMethods = []string{"GET", "POST", "PUT", "DELETE", "OPTIONS"}
	config.AllowHeaders = []string{"Origin", "Content-Type", "Accept", "Authorization"}
	r.Use(cors.New(config))

	// Add middleware for logging and performance
	r.Use(gin.Logger())
	r.Use(gin.Recovery())
	r.Use(cacheMiddleware())

	// Health check endpoint
	r.GET("/health", healthCheck)

	// API routes
	api := r.Group("/api")
	{
		api.GET("/all", getAllWeapons)
		api.GET("/categories", getCategories)
		api.GET("/category/:category", getWeaponsByCategory)
		api.GET("/weapon/:id", getWeaponByID)
		api.GET("/search", searchWeapons)
		api.GET("/stats", getStats)
		api.GET("/tier/:tier", getWeaponsByTier)
		api.GET("/skill/:skill", getWeaponsBySkill)
		api.GET("/requirements", getWeaponsByRequirements)
	}

	// Get port from environment or use default
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}

	log.Printf("Server starting on port %s", port)
	if err := r.Run(":" + port); err != nil {
		log.Fatal("Failed to start server:", err)
	}
}

func loadData() error {
	// Load weapons data - try comprehensive first, fallback to original
	weaponsData, err := os.ReadFile("data/weapons_comprehensive.json")
	if err != nil {
		log.Println("Comprehensive weapons file not found, trying original weapons.json")
		weaponsData, err = os.ReadFile("data/weapons.json")
		if err != nil {
			return err
		}
	}

	if err := json.Unmarshal(weaponsData, &weapons); err != nil {
		return err
	}

	// Load categories data
	categoriesData, err := os.ReadFile("data/categories.json")
	if err != nil {
		return err
	}

	if err := json.Unmarshal(categoriesData, &categories); err != nil {
		return err
	}

	log.Printf("Loaded %d weapons and %d categories", len(weapons), len(categories))
	return nil
}

func healthCheck(c *gin.Context) {
	c.JSON(http.StatusOK, models.APIResponse{
		Success: true,
		Data: gin.H{
			"status":    "healthy",
			"timestamp": time.Now().UTC(),
			"version":   "2.0.0",
			"weapons":   len(weapons),
			"categories": len(categories),
		},
	})
}

func getAllWeapons(c *gin.Context) {
	c.JSON(http.StatusOK, models.APIResponse{
		Success: true,
		Data:    weapons,
	})
}

func getCategories(c *gin.Context) {
	c.JSON(http.StatusOK, models.APIResponse{
		Success: true,
		Data:    categories,
	})
}

func getWeaponsByCategory(c *gin.Context) {
	category := c.Param("category")
	
	if category == "all" {
		c.JSON(http.StatusOK, models.APIResponse{
			Success: true,
			Data:    weapons,
		})
		return
	}

	var filteredWeapons []models.Weapon
	for _, weapon := range weapons {
		if weapon.Category == category {
			filteredWeapons = append(filteredWeapons, weapon)
		}
	}

	c.JSON(http.StatusOK, models.APIResponse{
		Success: true,
		Data:    filteredWeapons,
	})
}

func getWeaponByID(c *gin.Context) {
	idStr := c.Param("id")
	id, err := strconv.Atoi(idStr)
	if err != nil {
		c.JSON(http.StatusBadRequest, models.APIResponse{
			Success: false,
			Error:   "Invalid weapon ID",
		})
		return
	}

	for _, weapon := range weapons {
		if weapon.ID == id {
			c.JSON(http.StatusOK, models.APIResponse{
				Success: true,
				Data:    weapon,
			})
			return
		}
	}

	c.JSON(http.StatusNotFound, models.APIResponse{
		Success: false,
		Error:   "Weapon not found",
	})
}

func searchWeapons(c *gin.Context) {
	query := strings.ToLower(c.Query("q"))
	if query == "" {
		c.JSON(http.StatusBadRequest, models.APIResponse{
			Success: false,
			Error:   "Search query is required",
		})
		return
	}

	var results []models.Weapon
	for _, weapon := range weapons {
		if strings.Contains(strings.ToLower(weapon.Name), query) ||
			strings.Contains(strings.ToLower(weapon.Skill), query) ||
			strings.Contains(strings.ToLower(weapon.Description), query) {
			results = append(results, weapon)
		}
	}

	c.JSON(http.StatusOK, models.APIResponse{
		Success: true,
		Data:    results,
	})
}

func getStats(c *gin.Context) {
	stats := gin.H{
		"total_weapons": len(weapons),
		"categories":    len(categories),
		"weapon_types":  make(map[string]int),
		"tiers":         make(map[string]int),
		"skills":        make(map[string]int),
	}

	for _, weapon := range weapons {
		stats["weapon_types"].(map[string]int)[weapon.Type]++
		if weapon.Tier != "" {
			stats["tiers"].(map[string]int)[weapon.Tier]++
		}
		stats["skills"].(map[string]int)[weapon.Skill]++
	}

	c.JSON(http.StatusOK, models.APIResponse{
		Success: true,
		Data:    stats,
	})
}

func getWeaponsByTier(c *gin.Context) {
	tier := c.Param("tier")
	
	var filteredWeapons []models.Weapon
	for _, weapon := range weapons {
		if strings.EqualFold(weapon.Tier, tier) {
			filteredWeapons = append(filteredWeapons, weapon)
		}
	}

	c.JSON(http.StatusOK, models.APIResponse{
		Success: true,
		Data:    filteredWeapons,
	})
}

func getWeaponsBySkill(c *gin.Context) {
	skill := c.Param("skill")
	
	var filteredWeapons []models.Weapon
	for _, weapon := range weapons {
		if strings.Contains(strings.ToLower(weapon.Skill), strings.ToLower(skill)) {
			filteredWeapons = append(filteredWeapons, weapon)
		}
	}

	c.JSON(http.StatusOK, models.APIResponse{
		Success: true,
		Data:    filteredWeapons,
	})
}

func getWeaponsByRequirements(c *gin.Context) {
	// Parse query parameters for stat requirements
	strength, _ := strconv.Atoi(c.Query("strength"))
	dexterity, _ := strconv.Atoi(c.Query("dexterity"))
	intelligence, _ := strconv.Atoi(c.Query("intelligence"))
	faith, _ := strconv.Atoi(c.Query("faith"))
	arcane, _ := strconv.Atoi(c.Query("arcane"))

	var filteredWeapons []models.Weapon
	for _, weapon := range weapons {
		if weapon.Requirements.Strength <= strength &&
			weapon.Requirements.Dexterity <= dexterity &&
			weapon.Requirements.Intelligence <= intelligence &&
			weapon.Requirements.Faith <= faith &&
			weapon.Requirements.Arcane <= arcane {
			filteredWeapons = append(filteredWeapons, weapon)
		}
	}

	c.JSON(http.StatusOK, models.APIResponse{
		Success: true,
		Data:    filteredWeapons,
	})
}

func cacheMiddleware() gin.HandlerFunc {
	return func(c *gin.Context) {
		// Add cache headers for static data
		if strings.HasPrefix(c.Request.URL.Path, "/api/categories") ||
			strings.HasPrefix(c.Request.URL.Path, "/api/all") {
			c.Header("Cache-Control", "public, max-age=3600") // 1 hour
		}
		c.Next()
	}
}