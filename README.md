# **Digital Transformation and Carbon Emissions: The Mediating Role of Environmental Innovation**

### **Overview**

This repository supports the research project **“Digital Transformation and Carbon Emissions: The Mediating Role of Environmental Innovation.”** It provides tools to quantify **Environmental Innovation** (EI) by analyzing the **Management Discussion and Analysis (MDA)** sections of companies’ yearbooks.

Leveraging **large language models (LLMs)** from [Modelscope](https://www.modelscope.cn/) and [Hugging Face Transformers](https://huggingface.co/docs/transformers/), this repository enables:

- Summarization and translation of yearbook content.

- Construction of a custom corpus with raw MDA data and labeled EI metrics (dummy or degree).

- Automated and scalable methods for sustainability research.

### **Repository Structure**

- README.md: Project overview, usage guide, and references.
- /data: Corpus containing raw MDA data and labeled Environmental Innovation metrics.
- /code: Python scripts for data preprocessing, summarization, translation, and EI extraction.
- /models: Pre-trained and fine-tuned LLMs for summarization and EI prediction.
- requirements.txt: Python dependencies required to run the project.

### **Features**

**1.**	**Summarization and Translation** :

- Automatically extract key information from MDAs using [Modelscope](https://www.modelscope.cn/) and [Hugging Face Transformers](https://huggingface.co/docs/transformers).

**2.**	**Environmental Innovation Metrics** :

- Label MDAs with dummy variables or degrees of EI using LLMs and human-marked data.

**3.**	**Corpus Construction** :

- Generate and store a labeled dataset for training and evaluation.

**4.**	**Customizable Workflow** :

- Flexible tools to adapt to different datasets, languages, and business contexts.

### **Getting Started (suggested)**

**1. Clone the Repository**

git clone https://github.com/xinihe/ESG_Agent.git

**2. Create a Virtual Environment**

python -m venv esg_venv

source esg_venv/bin/activate

**3. Install Dependencies**

pip install -r requirements.txt

### **Tutorial**

**Step 1: Summarize MDA Content**


**Step 2: Translate MDA Content**


**Step 3: Quantify Environmental Innovation**


**Step 4: Train a Custom LLM (Optional)**


### **References**
