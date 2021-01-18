# Dockerfile                                                                    
from python:3.6.6                                                               
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONBUFFERED=1
                                                                                
WORKDIR /                                                                       
ENV FLASK_APP=app.py                                                            
ENV FLASK_RUN_HOST=0.0.0.0                                                      
COPY requirements.txt ./                                                        
RUN pip install --no-cache-dir -r requirements.txt                              
RUN rm requirements.txt                                                         
                                                                                
WORKDIR /app                                                                        
