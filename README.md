# Post-Quantum Cryptography Web Application

This Flask web application demonstrates Post-Quantum Cryptography (PQC) techniques for encrypting and decrypting data. It implements the Kyber algorithm, a lattice-based encryption scheme that is a finalist in NIST's Post-Quantum Cryptography standardization process.

## Features

- Generate quantum-resistant public/private key pairs
- Encrypt messages using the public key
- Decrypt messages using the private key
- Secure web interface with proper error handling

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/pqc-webapp.git
cd pqc-webapp
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - On Windows:
   ```bash
   venv\Scripts\activate
   ```
   - On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

6. Run the application:
```bash
python run.py
```

7. Open your browser and navigate to `http://127.0.0.1:5000`

## Project Structure

```
pqc_webapp/
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore file
├── README.md              # Project documentation
├── app/                   # Application package
│   ├── __init__.py        # App initialization
│   ├── config.py          # Configuration settings
│   ├── crypto/            # Cryptography module
│   │   ├── __init__.py
│   │   └── pqc.py         # Post-quantum crypto implementation
│   ├── routes/            # Web routes
│   │   ├── __init__.py
│   │   └── main.py        # Main routes
│   ├── static/            # Static assets
│   │   ├── css/           # CSS styles
│   │   └── js/            # JavaScript files
│   └── templates/         # HTML templates
│       ├── base.html      # Base template
│       └── index.html     # Homepage template
├── requirements.txt       # Project dependencies
└── run.py                 # Application entry point
```

## Security Features

- Implements Kyber encryption, a NIST PQC finalist
- Uses Flask-Talisman for secure HTTP headers
- Implements input validation and proper error handling
- CSRF protection using Flask-WTF

## Algorithm Details

This application uses the Kyber algorithm for post-quantum encryption. Kyber is a module lattice-based key encapsulation mechanism (KEM) that is considered secure against attacks from both classical and quantum computers.

- **Key Generation**: Creates a public/private key pair
- **Encryption**: Uses the public key to encrypt a message
- **Decryption**: Uses the private key to decrypt the ciphertext

## Contributors

- [Qasim Saeed]
- [Hakim Ali]
