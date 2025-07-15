# Elden Ring Weapon API

A high-performance REST API for Elden Ring weapon data, built with Go and Gin framework.

## Features

- **Comprehensive Weapon Data**: Accurate weapon information from official Elden Ring sources
- **Multiple Endpoints**: Search, filter, and retrieve weapon data
- **High Performance**: Optimized Go code with caching
- **Docker Support**: Easy deployment with Docker
- **Health Monitoring**: Built-in health checks
- **CORS Support**: Cross-origin resource sharing enabled

## API Endpoints

### Core Endpoints

- `GET /health` - Health check and API status
- `GET /api/all` - Get all weapons
- `GET /api/categories` - Get weapon categories
- `GET /api/category/:category` - Get weapons by category
- `GET /api/weapon/:id` - Get weapon by ID

### Search & Filter Endpoints

- `GET /api/search?q=query` - Search weapons by name, skill, or description
- `GET /api/tier/:tier` - Get weapons by tier
- `GET /api/skill/:skill` - Get weapons by skill
- `GET /api/requirements?strength=10&dexterity=15` - Get weapons by stat requirements
- `GET /api/stats` - Get API statistics

## Data Structure

### Weapon Object
```json
{
  "id": 1,
  "name": "Uchigatana",
  "type": "Katana",
  "category": "katanas",
  "skill": "Unsheathe",
  "weight": 5.5,
  "requirements": {
    "strength": 11,
    "dexterity": 15,
    "intelligence": 0,
    "faith": 0,
    "arcane": 0
  },
  "scaling": {
    "strength": "D",
    "dexterity": "D",
    "intelligence": "-",
    "faith": "-",
    "arcane": "-"
  },
  "stats": {
    "physical": 115,
    "magic": 0,
    "fire": 0,
    "lightning": 0,
    "holy": 0,
    "critical": 100,
    "guard_boost": 0
  },
  "description": "A katana with a long single-edged curved blade...",
  "location": "Deathtouched Catacombs, Limgrave"
}
```

## Quick Start

### Prerequisites
- Go 1.21 or higher
- Docker (optional)

### Local Development

1. Clone the repository
2. Navigate to the backend directory
3. Install dependencies:
   ```bash
   go mod download
   ```
4. Run the server:
   ```bash
   go run main.go
   ```

The API will be available at `http://localhost:8080`

### Docker Deployment

1. Build the Docker image:
   ```bash
   docker build -t elden-ring-api .
   ```

2. Run the container:
   ```bash
   docker run -p 8080:8080 elden-ring-api
   ```

### Environment Variables

- `PORT` - Server port (default: 8080)
- `GIN_MODE` - Gin mode (debug/release)

## Performance Optimizations

- **In-Memory Data Loading**: Data is loaded once at startup
- **Caching Headers**: Static data endpoints include cache headers
- **Efficient Filtering**: Optimized search and filter algorithms
- **Minimal Dependencies**: Lightweight Go modules

## Data Sources

All weapon data is sourced from official Elden Ring game files and verified community resources to ensure accuracy.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is unofficial and not affiliated with Bandai Namco Entertainment. Elden Ring is a trademark of Bandai Namco Entertainment.