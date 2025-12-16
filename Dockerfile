#Dockefile

FROM apache/airflow:2.10.4-python3.12

USER root

# Copia o Instant Client
COPY oracle_client/instantclient_21_13/instantclient_21_13 /opt/oracle/instantclient_21_13

# Fix apt repository URLs
RUN sed -i 's|http://deb.debian.org|https://deb.debian.org|g' /etc/apt/sources.list.d/debian.sources \
    && sed -i 's|http://snapshot.debian.org|https://snapshot.debian.org|g' /etc/apt/sources.list.d/debian.sources


# Instala dependências
RUN apt-get update && \
    apt-get install -y  libaio1 libaio-dev libnsl2 unzip && \
    rm -rf /var/lib/apt/lists/*

# Registra o Instant Client no sistema
RUN echo /opt/oracle/instantclient_21_13 > /etc/ld.so.conf.d/oracle-instantclient.conf && \
    ldconfig

# Variáveis de ambiente
ENV LD_LIBRARY_PATH="/opt/oracle/instantclient_21_13:${LD_LIBRARY_PATH}"
ENV PATH="${PATH}:/opt/oracle/instantclient_21_13"
ENV ORACLE_HOME="/opt/oracle/instantclient_21_13"


USER airflow
RUN pip install --upgrade pip

RUN pip install pandas \
               requests==2.32.3 \
               apache-airflow-providers-google==10.19.0 \
               openpyxl==3.1.5 \
               gspread==6.0.0 \
               oracledb==3.4.1 \
               apache-airflow-providers-oracle==4.2.0


