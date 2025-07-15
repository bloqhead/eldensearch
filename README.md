# Elden Ring Weapon Search

A comprehensive weapon database and search application for Elden Ring, featuring accurate data from official sources and a modern, responsive interface.

## 🎯 Features

### Frontend (Vue 3 + TypeScript)
- **Modern UI**: Clean, responsive design with Tailwind CSS
- **Real-time Search**: Instant weapon search by name, skill, or description
- **Category Filtering**: Filter weapons by type (Katanas, Greatswords, etc.)
- **Detailed Weapon Cards**: Complete weapon information including stats, scaling, and requirements
- **Pagination**: Efficient handling of large datasets
- **Mobile Responsive**: Optimized for all device sizes

### Backend (Go + Gin)
- **High Performance**: Optimized Go API with in-memory data loading
- **Comprehensive Endpoints**: Multiple search and filter options
- **Caching**: Built-in caching for static data
- **Health Monitoring**: Health check endpoints
- **Docker Support**: Easy deployment with Docker
- **CORS Enabled**: Cross-origin resource sharing support

### Data Accuracy
- **Official Sources**: Data sourced from official Elden Ring game files
- **Comprehensive Coverage**: All weapon types, stats, scaling, and requirements
- **Regular Updates**: Maintained with latest game patches and DLC content

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ and pnpm (for frontend)
- Go 1.21+ (for backend)
- Docker (optional)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install Go dependencies:
   ```bash
   go mod download
   ```

3. Run the server:
   ```bash
   go run main.go
   ```

The API will be available at `http://localhost:8080`

### Frontend Setup

1. Install dependencies:
   ```bash
   pnpm install
   ```

2. Start the development server:
   ```bash
   pnpm dev
   ```

The application will be available at `http://localhost:5173`

### Docker Deployment

1. Build and run the backend:
   ```bash
   cd backend
   docker build -t elden-ring-api .
   docker run -p 8080:8080 elden-ring-api
   ```

2. Build and run the frontend:
   ```bash
   pnpm build
   # Serve the dist folder with your preferred web server
   ```

## 📊 API Endpoints

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

## 🗃️ Data Structure

### Weapon Object
```typescript
{
  id: number
  name: string
  type: string
  category: string
  tier?: string
  skill: string
  weight: number
  requirements: {
    strength: number
    dexterity: number
    intelligence: number
    faith: number
    arcane: number
  }
  scaling: {
    strength: string
    dexterity: string
    intelligence: string
    faith: string
    arcane: string
  }
  stats: {
    physical: number
    magic: number
    fire: number
    lightning: number
    holy: number
    critical: number
    guard_boost: number
  }
  description: string
  location: string
}
```

## 🛠️ Technology Stack

### Frontend
- **Vue 3** - Progressive JavaScript framework
- **TypeScript** - Type-safe JavaScript
- **Vite** - Fast build tool and dev server
- **Tailwind CSS** - Utility-first CSS framework
- **FontAwesome** - Icon library

### Backend
- **Go 1.21** - High-performance programming language
- **Gin** - HTTP web framework
- **CORS** - Cross-origin resource sharing
- **Docker** - Containerization

## 📈 Performance Optimizations

### Backend
- **In-Memory Data Loading**: Data loaded once at startup
- **Caching Headers**: Static data endpoints include cache headers
- **Efficient Filtering**: Optimized search algorithms
- **Minimal Dependencies**: Lightweight Go modules

### Frontend
- **Lazy Loading**: Components loaded on demand
- **Efficient Rendering**: Vue 3's Composition API
- **Optimized Build**: Vite's fast build process
- **Responsive Design**: Mobile-first approach

## 🔧 Development

### Project Structure
```
├── backend/                 # Go API server
│   ├── main.go             # Main server file
│   ├── models/             # Data models
│   ├── data/               # JSON data files
│   ├── Dockerfile          # Docker configuration
│   └── README.md           # Backend documentation
├── src/                    # Vue frontend source
│   ├── components/         # Vue components
│   ├── types.ts           # TypeScript types
│   └── App.vue            # Main application
├── public/                 # Static assets
└── README.md              # Project documentation
```

### Adding New Weapons
1. Edit `backend/data/weapons.json`
2. Add weapon data following the established structure
3. Restart the backend server

### Adding New Categories
1. Edit `backend/data/categories.json`
2. Add category data
3. Update weapons to use the new category
4. Restart the backend server

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is unofficial and not affiliated with Bandai Namco Entertainment. Elden Ring is a trademark of Bandai Namco Entertainment.

## 🙏 Acknowledgments

- **Bandai Namco Entertainment** for creating Elden Ring
- **FromSoftware** for the incredible game design
- **Elden Ring Community** for data verification and feedback

## 📞 Support

If you encounter any issues or have questions:
1. Check the existing issues
2. Create a new issue with detailed information
3. Include steps to reproduce the problem

---

**Note**: This project is maintained by fans for fans. All weapon data is sourced from official game files and verified community resources to ensure accuracy.
