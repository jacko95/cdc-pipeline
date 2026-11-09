<div align="center">
  <h1>CDC Pipeline</h1>
  <p><strong>Change Data Capture in tempo reale da MySQL a Kafka, con elaborazione Flink e Spark.</strong></p>

<p>
    <img src="https://img.shields.io/badge/Apache-Kafka-231F20?logo=apache-kafka&logoColor=white" alt="Kafka"/>
    <img src="https://img.shields.io/badge/Debezium-CDC-orange" alt="Debezium"/>
    <img src="https://img.shields.io/badge/Apache-Flink-E6526F?logo=apache-flink&logoColor=white" alt="Flink"/>
    <img src="https://img.shields.io/badge/Apache-Spark-E25A1C?logo=apache-spark&logoColor=white" alt="Spark"/>
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"/>
  </p>
</div>

## 📱 Cos'è CDC Pipeline?

**CDC Pipeline** è un progetto dimostrativo che implementa un flusso di **Change Data Capture** end-to-end:

- Cattura in tempo reale le modifiche (INSERT, UPDATE, DELETE) da un database **MySQL**
- Le pubblica su **Apache Kafka** tramite **Debezium** e Kafka Connect
- Le elabora con diversi framework: **Apache Flink** (Java) e **Apache Spark** (Python)
- Espone i risultati tramite **FastAPI** e una dashboard **Flask**
- Usa **Nginx** come reverse proxy davanti ai servizi web

È pensato come ambiente di apprendimento per CDC, Kafka, stream processing e microservizi.

> **Nota:** Questo progetto utilizza **solo immagini ufficiali** (Apache Kafka, Debezium, Flink, Spark, ecc.).
> Su GitHub si trovano spesso soluzioni basate sulle immagini **Confluent**.

## ✨ Componenti principali

| Componente | Descrizione |
|-----------|-------------|
| **MySQL** | Database sorgente con schema di esempio |
| **Debezium + Kafka Connect** | Cattura le modifiche del database |
| **Apache Kafka** | Backbone di messaggistica |
| **Apache Flink** | Stream processing in Java |
| **Apache Spark** | Elaborazione batch in Python |
| **FastAPI** | API REST che consuma gli eventi |
| **Flask** | API REST che consuma gli eventi |
| **Nginx** | Reverse proxy per i servizi web |

## 🏗 Architettura

<div align="center">
  <img src="https://nurebo-public.s3.eu-central-1.amazonaws.com/images/architettura2.jpg" alt="CDC Pipeline Architecture" width="800"/>
</div>

### Flusso dei dati

1. Una modifica avviene su MySQL
2. Debezium cattura l'evento e lo pubblica su un topic Kafka
3. Flink e Spark consumano e elaborano gli eventi
4. I risultati vengono inviati a FastAPI e Flask per essere esposti
5. Nginx fa da reverse proxy davanti ai servizi web

## 🛠 Tech Stack

**CDC & Messaging**
Apache Kafka · Debezium · Kafka Connect · Zookeeper

**Elaborazione**
Apache Flink (Java) · Apache Spark (Python)

**API & Web**
FastAPI · Flask · Nginx

**Infrastruttura**
Docker · MySQL · CloudFormation

## 🚀 Come iniziare

### Prerequisiti

- Docker e Docker Compose
- Almeno 8 GB di RAM disponibili

### Avvio

```bash
git clone https://github.com/jacko95/cdc-pipeline.git
cd cdc-pipeline
docker-compose up -d
```

### Test

```bash
chmod +x init-connector.sh
./init-connector.sh
```

## 📁 Struttura del progetto

```text
cdc-pipeline/
├── fastAPI/              # Servizio FastAPI (consumer + API)
├── flask/                # Servizio Flask (riceve eventi via POST)
├── flink/                # Job Flink (Java)
├── spark/                # Applicazioni Spark (Python)
├── mysql/                # Schema e init scripts
├── nginx/                # Configurazione Nginx (reverse proxy)
├── docker-compose.yml    # Orchestrazione servizi
├── init-connector.sh     # Registrazione Debezium connector
└── deploy.cf.yaml        # Template CloudFormation (opzionale)
```

## 📄 Licenza

Questo progetto è rilasciato sotto la **MIT License**.

---

<div align="center">
  <p>Realizzato con ❤️ in Kafka, Flink e Spark</p>
  <p><strong>CDC Pipeline</strong> — Change Data Capture in tempo reale.</p>
</div>
