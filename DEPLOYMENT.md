# Deployment Guide for Render

This guide will help you deploy the Elden Ring Weapon Search application to Render.

## Prerequisites

1. A Render account (free tier available)
2. Your FontAwesome Pro token
3. This repository connected to your Render account

## Deployment Steps

### 1. Connect Repository to Render

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New +" and select "Blueprint"
3. Connect your GitHub repository
4. Render will automatically detect the `render.yaml` file

### 2. Configure Environment Variables

After the services are created, you'll need to set the FontAwesome token:

1. Go to the **eldensearch-frontend** service
2. Navigate to "Environment" tab
3. Add environment variable:
   - **Key**: `FONTAWESOME_TOKEN`
   - **Value**: Your FontAwesome Pro token

### 3. Deploy Services

1. **Backend Service** (`eldensearch-backend`):
   - Will be deployed automatically
   - Available at: `https://eldensearch-backend.onrender.com`
   - Health check: `/health` endpoint

2. **Frontend Service** (`eldensearch-frontend`):
   - Will be deployed automatically
   - Available at: `https://eldensearch-frontend.onrender.com`
   - Configured to use the backend service

### 4. Update Frontend API URL (if needed)

If the backend service URL changes, update the `VITE_API_URL` environment variable in the frontend service to match the new backend URL.

## Service Configuration

### Backend Service
- **Type**: Web Service
- **Environment**: Docker
- **Port**: 7342
- **Health Check**: `/health`
- **Plan**: Starter (free tier)

### Frontend Service
- **Type**: Web Service
- **Environment**: Docker
- **Port**: 80 (nginx)
- **Plan**: Starter (free tier)

## Environment Variables

### Backend
- `GIN_MODE`: `release`
- `PORT`: `7342`

### Frontend
- `FONTAWESOME_TOKEN`: Your FontAwesome Pro token (set manually)
- `VITE_API_URL`: Backend service URL (auto-configured)

## Troubleshooting

### Build Issues
- Check the build logs in Render dashboard
- Ensure FontAwesome token is set correctly
- Verify all environment variables are configured

### Runtime Issues
- Check service logs in Render dashboard
- Verify health check endpoints are responding
- Ensure frontend can reach backend service

### Performance
- Consider upgrading to paid plans for better performance
- Monitor resource usage in Render dashboard

## Cost

- **Free Tier**: Both services can run on free tier
- **Paid Plans**: Available for better performance and features

## Support

For Render-specific issues, check the [Render Documentation](https://render.com/docs). 