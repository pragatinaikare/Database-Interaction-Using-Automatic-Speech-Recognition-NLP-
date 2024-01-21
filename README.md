# Interactive Multilingual SQL Interface

Welcome to our innovative project that empowers users with no prior knowledge of SQL to interact with databases effortlessly using their own language. Our system currently supports three languages: English, French, and German.

## Key Features
### 1. Speech to Text Conversion
We leverage the SpeechRecognition library in Python to capture audio from the microphone and utilize the Google Web Speech API for speech-to-text conversion. Users can simply speak their queries, and the system will transform them into text.

### 2. Text to SQL Query
The system employs NLTK for tokenization and SpaCy for Named Entity Recognition (NER) to extract entities and relationships from the textual query. The result is then processed by ln2sql for SQL query generation.

### 3. SQL Query Generation
Named Entity Recognition with SpaCy plays a pivotal role in identifying and classifying entities within spoken queries. The entities of interest include table names, column names, and numeric values. The system intelligently maps these entities to SQL keywords, constructing meaningful SQL queries.

### 4. Real-Time Noise Reduction
Implemented real-time noise reduction algorithm before sending audio to the speech recognition API to enhance system's accuracy. Utilize signal processing library - librosa for effective noise reduction.

###  5. Database Interaction
Connected with a database engine MYSQL to execute the generated SQL query. The system displays query results in a tabular format.

## How to Use
### Speech Input:
Users can simply speak their queries into the system's microphone.
### Language Flexibility:
Engage with the system in English, French, or German for a personalized experience.
### Effortless Query Generation:
Witness the magic as the system converts spoken language into meaningful SQL queries and returns the output in tabular format.


## Contributions
We welcome contributions from the open-source community to enhance and expand the capabilities of this project. Feel free to submit issues, pull requests, or suggestions.

## License
This project is licensed under the MIT License, making it open and accessible for collaboration.
