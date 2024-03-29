FROM python:3.10
EXPOSE 8501
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY data_creation.py ./data_creation.py
COPY data_preprocessing.py ./data_preprocessing.py
COPY model_preparation.py ./model_preparation.py
COPY model_testing.py ./model_testing.py
COPY pipeline.sh ./pipeline.sh
RUN chmod u+r+x pipeline.sh
CMD ["bash", "pipeline.sh"]
