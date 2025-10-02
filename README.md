# 🚀 PyWebView + Svelte 5 Template

A modern template for creating desktop applications with Python (backend) and Svelte 5 + TypeScript (frontend).

## ✨ Features

- **Python Backend** with Flask and pywebview
- **Svelte 5 Frontend** with TypeScript
- **REST API** for frontend-backend communication
- **Real-time state management**
- **Automated build scripts**
- **Development mode** with hot-reload and external connections
- **Automated linting and formatting** (ESLint 9 + Prettier)
- **Flexible configuration** via environment variables

## 🛠️ Technologies Used

### Backend

- **Python 3.8+**
- **pywebview** - Desktop window creation
- **Flask** - Web framework
- **Flask-CORS** - CORS handling

### Frontend

- **Svelte 5** - Modern JavaScript framework
- **TypeScript** - Static typing
- **Tailwind CSS 4.1.x** - Utility CSS framework
- **Vite** - Fast build tool
- **Axios** - HTTP client
- **ESLint 9** - JavaScript/TypeScript linter (flat config)
- **Prettier** - Code formatter
- **Pylint** - Python linter

## 📋 Prerequisites

- **Python 3.8+**
- **Node.js 16+**
- **pnpm**

## 🚀 Installation and Setup

### 1. Clone the project

```bash
git clone <your-repo>
cd template-pywebview-svelte
```

### 2. Install dependencies

#### Python Backend

```bash
pip install -r requirements.txt
```

#### Node.js Frontend

```bash
# With pnpm (recommended)
pnpm install

# Or with npm
npm install
```

### 3. Launch the application

#### Production mode (recommended)

```bash
python run.py
```

#### Development mode

```bash
python dev.py
```

The Vite server starts automatically with the `--host` option to allow external connections. If `localhost:3000` doesn't work, use the IP displayed by Vite (e.g., `http://172.31.247.210:3000/`).

### 4. Development Scripts

#### Linting and Formatting

```bash
# JavaScript/TypeScript linter (ESLint 9)
pnpm run lint

# Automatic linting error correction
pnpm run lint:fix

# Code formatting with Prettier
pnpm run format

# Format checking
pnpm run format:check

# Python linter (optional)
pylint app.py run.py dev.py build_exe.py config.py
```

#### Build and Verification

```bash
# Frontend build
pnpm run build

# TypeScript verification
pnpm run check

# Watch mode verification
pnpm run check:watch
```

## 📁 Project Structure

```
template-pywebview-svelte/
├── 📁 src/                    # Svelte source code
│   ├── 📁 components/         # Svelte components
│   │   ├── Header.svelte
│   ├── 📁 lib/               # Utilities and services
│   │   └── api.ts           # API service
│   ├── App.svelte           # Main component
│   ├── main.ts             # Entry point
│   └── app.css             # Global styles
├── 📁 dist/                 # Frontend build (generated)
├── app.py                  # Main Python application
├── config.py               # Centralized configuration
├── run.py                  # Launch script
├── dev.py                  # Development script
├── build_exe.py            # Executable build script
├── requirements.txt        # Python dependencies
├── package.json           # Node.js dependencies
├── vite.config.ts         # Vite configuration (with --host)
├── tsconfig.json          # TypeScript configuration
├── eslint.config.cjs      # ESLint 9 configuration (flat config)
└── README.md              # Documentation
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file at the project root:

```env
# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
PORT=5000
HOST=127.0.0.1

# Window Configuration
WINDOW_TITLE=PyWebView + Svelte Application
WINDOW_WIDTH=1200
WINDOW_HEIGHT=800
```

### Window Customization

Modify settings in `config.py` or via environment variables:

```python
# In config.py
WINDOW_TITLE = 'Your Application'
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
WINDOW_MIN_SIZE = (800, 600)
```

Or via the `.env` file:

```env
WINDOW_TITLE=Your Application
WINDOW_WIDTH=1200
WINDOW_HEIGHT=800
```

## 🎯 API Endpoints

### API Health

- **GET** `/api/health` - Check API status

### Messages

- **GET** `/api/message` - Get current message
- **POST** `/api/message` - Update message

### Items

- **GET** `/api/items` - Get items list
- **POST** `/api/items` - Add new item
- **DELETE** `/api/items/{id}` - Delete item

## 🎨 Customization

### CSS Styles

Styles are organized in `src/app.css` with CSS variables:

```css
:root {
  --primary-color: #3498db;
  --secondary-color: #2ecc71;
  --danger-color: #e74c3c;
  /* ... other variables */
}
```

### Svelte Components

Each component is in `src/components/` and can be customized according to your needs.

### Backend API

Add new endpoints in `app.py`:

```python
@app.route('/api/your-endpoint')
def your_function():
    return jsonify({'data': 'your_data'})
```

## 🚀 Deployment

### Production Build

```bash
# Build frontend
pnpm run build

# Launch application
python run.py
```

### Executable Creation

To create an executable with PyInstaller:

```bash
# Windows
build.bat

# Linux/Mac
python build_exe.py
```

The executable will be created in the `dist/` folder with all files integrated.

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use error**
   - Change the port in `config.py` or `app.py`

2. **Missing dependencies**
   - Verify all dependencies are installed
   - Run `pip install -r requirements.txt` and `pnpm install`

3. **Frontend build error**
   - Verify Node.js is installed
   - Run `pnpm install` then `pnpm run build`

4. **Vite server not accessible from outside**
   - The `dev.py` script automatically uses `--host`
   - If `localhost:3000` doesn't work, use the IP displayed by Vite

5. **pywebview error with unsupported parameters**
   - Some parameters like `minimizable` and `maximizable` are not supported

6. **ESLint or Pylint errors**
   - ESLint 9 uses the new "flat config" configuration
   - Pylint errors can be fixed with `pylint --disable=W0212 app.py`

### Logs and Debugging

- Enable debug mode in `config.py`
- Check the console for errors
- Use browser development tools

## 📚 Useful Resources

- [pywebview Documentation](https://pywebview.flowrl.com/)
- [Svelte Documentation](https://svelte.dev/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [TypeScript Documentation](https://www.typescriptlang.org/docs/)

## 🤝 Contributing

1. Fork the project
2. Create a branch for your feature
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## 🙏 Acknowledgments

- [pywebview](https://github.com/r0x0r/pywebview) for desktop integration
- [Svelte](https://svelte.dev/) for the frontend framework
- [Flask](https://flask.palletsprojects.com/) for the Python backend
