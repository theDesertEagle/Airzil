# AIRZIL ENVIRONMENT - Image recipe

# Setup base environment with Miniconda and Python 3.7.4
FROM continuumio/miniconda3:4.7.12

# Update package information, conda and installing 'ps' command
RUN apt-get update && \
	apt-get install procps -y

RUN	conda update -n base -c defaults conda

# Create conda environment along with dependencies
RUN conda create -y --name airzil python=3.7.4 \
	numpy \
	pandas \
	matplotlib \
	seaborn \
	scikit-learn \
	dash-renderer \
	dash \
	dash-html-components \
	dash-core-components \
	plotly \
	notebook \
	jupyterlab \
	ipywidgets \
	jupyter_contrib_nbextensions \
	-c pytorch -c defaults -c conda-forge

# Navigate to project working directory
WORKDIR /home/airzil

# Activate conda environment on every shell run
RUN echo "conda activate airzil" >> ~/.bashrc
ENV PATH /opt/conda/envs/airzil/bin:$PATH