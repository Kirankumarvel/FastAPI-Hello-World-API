# FastAPI Hello World API

A simple FastAPI application demonstrating basic API endpoints with automatic documentation.

---

## 🚀 Features

- FastAPI framework with automatic OpenAPI documentation
- Two endpoints: root path and personalized welcome message
- Interactive API docs at `/docs` and `/redoc`
- Python 3.7+ compatibility
- Virtual environment setup

---

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kirankumarvel/fastapi-hello-world-api.git
   cd fastapi-hello-world-api
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 📦 Dependencies

- `fastapi` - Web framework for building APIs
- `uvicorn` - ASGI server for running FastAPI apps

To generate `requirements.txt`:
```bash
pip freeze > requirements.txt
```

---

## 🚀 Running the Application

1. **Start the development server**
   ```bash
   uvicorn main:app --reload --reload-exclude venv
   ```

2. **Access the application**
   - API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - Interactive docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Alternative docs: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📡 API Endpoints

### `GET /`
Returns a simple hello world message.

**Response:**
```json
{
  "message": "Hello World!"
}
```

---

### `GET /welcome`
Returns a personalized welcome message.

**Parameters:**
- `name` (optional): Name of the user (default: "Guest")

**Example:**
```bash
curl "http://127.0.0.1:8000/welcome?name=John"
```

**Response:**
```json
{
  "Message": "Hello, John! Welcome to our API."
}
```

---

## 🧪 Testing the API

- **Web browser:** Visit the endpoints directly
- **curl:**
  ```bash
  curl http://127.0.0.1:8000/
  curl "http://127.0.0.1:8000/welcome?name=Alice"
  ```
- **Interactive documentation:** Use the Swagger UI at `/docs`

---

## 📁 Project Structure

```
fastapi-hello-world-api/
├── main.py          # Main application file
├── requirements.txt # Project dependencies
├── README.md        # Project documentation
└── venv/            # Virtual environment (gitignored)
```

---

## 🔧 Troubleshooting

### Common Issues

1. **Permission denied when creating venv**
   ```bash
   # Run as administrator or use:
   python -m venv venv --without-pip
   ```

2. **Module not found error**
   - Ensure you're in the correct directory containing `main.py`
   - Check that the virtual environment is activated

3. **Reload issues due to venv changes**
   ```bash
   # Use the exclude flag:
   uvicorn main:app --reload --reload-exclude venv
   ```

---

## 📚 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

---

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- FastAPI team for the excellent framework
- Uvicorn team for the ASGI server
- Python community for ongoing support

---

## Additional GitHub Files

### `.gitignore`
<details>
<summary>Click to expand</summary>

```
# Virtual environment
venv/
.env

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```
</details>

### `requirements.txt`
<details>
<summary>Click to expand</summary>

```
fastapi==0.104.1
uvicorn==0.24.0
```
</details>
