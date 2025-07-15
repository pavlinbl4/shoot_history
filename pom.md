your_project/
│
├── pages/                 # Page Object classes
│   ├── base_page.py
│   └── login_page.py
│
├── tests/                 # Test cases
│   └── test_login.py
│
├── data/                  # Test data, input files, expected output files
│   ├── users.csv
│   └── sample_upload_file.txt
│
├── utils/                 # Helper scripts or programs
│   ├── file_manager.py    # Read/write/delete files
│   └── logger.py
│
├── downloads/             # Temporary download target (cleaned after tests)
│
├── uploads/               # Upload-ready files (e.g. for file input elements)
│
├── output/                # Screenshots, reports, logs, etc.
│
├── conftest.py            # Pytest fixtures
├── requirements.txt
└── pytest.ini
