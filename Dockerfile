FROM python:3.7.9
COPY . .
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
RUN pip install "uvicorn[standard]"
EXPOSE 5000
CMD ["uvicorn", "project.main:main", "--host", "0.0.0.0", "--port", "5000"]
#CMD ["flask", "run"]