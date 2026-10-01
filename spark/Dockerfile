FROM apache/spark:3.5.1-scala2.12-java17-python3-ubuntu
# FROM apache/spark:3.5.1

USER root

# Installa Python e dipendenze di sistema utili
RUN apt-get update && \
    apt-get install -y python3 python3-pip openjdk-17-jre-headless curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Aggiorna pip e installa PySpark (assicura la compatibilità)
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir requests && \
    pip3 install pyspark==3.5.1 py4j==0.10.9.7

# Crea directory di lavoro
WORKDIR /app

COPY app/kafka_to_http.py /opt/spark-apps/kafka_to_http.py

# Imposta le variabili d'ambiente per Spark
ENV SPARK_HOME=/opt/spark
#ENV PYTHONPATH=${SPARK_HOME}/python:${SPARK_HOME}/python/lib/py4j-0.10.9.7-src.zip:${PYTHONPATH}
ENV PYTHONPATH=/opt/spark/python:/opt/spark/python/lib/py4j-0.10.9.7-src.zip
ENV PATH=${SPARK_HOME}/bin:${PATH}

#USER 185


#FROM apache/spark:3.5.1-scala2.12-java17-python3-ubuntu
 #
 #USER root
 #
 #RUN apt-get update && \
 #    apt-get install -y python3 python3-pip curl && \
 #    apt-get clean && \
 #    rm -rf /var/lib/apt/lists/*
 #
 #RUN pip3 install --no-cache-dir requests
 #
 #WORKDIR /app
 #
 #COPY app/kafka_to_http.py /opt/spark-apps/kafka_to_http.py
 #
 #ENV SPARK_HOME=/opt/spark
 #ENV PATH=/opt/spark/bin:${PATH}