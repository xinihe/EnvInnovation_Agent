# **Digital Transformation and Carbon Emissions: The Mediating Role of Environmental Innovation**

### **Overview**

This repository supports the research project **“Digital Transformation and Carbon Emissions: The Mediating Role of Environmental Innovation.”** It provides tools to quantify **Environmental Innovation** (EI) by analyzing the **Management Discussion and Analysis (MDA)** sections of companies’ yearbooks.

Leveraging **large language models (LLMs)** from [Modelscope](https://www.modelscope.cn/) and [Hugging Face Transformers](https://huggingface.co/docs/transformers/), this repository enables:

- Summarization and translation of yearbook content.
- Construction of a custom corpus with raw MDA data and labeled EI metrics (dummy or degree).
- Automated and scalable methods for sustainability research.

### **Models** 

This section lists recommended LLMs from **Modelscope** and **Hugging Face Transformers** that are suited for summarization and translation tasks.

**1. Summarization Models (Modelscope)**

The following LLMs from Modelscope can summarize Chinese text effectively:

| **Model Name**                                                        | **Task**     | **Description**                                                       |
| --------------------------------------------------------------------------- | ------------------ | --------------------------------------------------------------------------- |
| [Ziya-LLaMA-13B](https://www.modelscope.cn/models/ziya/ziya-llama-13b/summary) | Text Summarization | A powerful LLaMA-based model trained for multi-language text summarization. |
| [mGLM-10B](https://www.modelscope.cn/models/mglm/mglm-10b)                     | Summarization      | A multilingual model optimized for concise and contextual summaries.        |
| [StructBERT](https://www.modelscope.cn/models/structbert/summary)              | Text Analysis      | Suitable for summarizing structured and unstructured data in Chinese.       |

**2. Translation Models (Hugging Face Transformers)**

The following LLMs from Hugging Face Transformers can translate Chinese text into English:

| **Model Name**                                                                          | **Task**             | **Description**                                                |
| --------------------------------------------------------------------------------------------- | -------------------------- | -------------------------------------------------------------------- |
| [Helsinki-NLP/opus-mt-zh-en](https://huggingface.co/Helsinki-NLP/opus-mt-zh-en)                  | Machine Translation        | Pre-trained model for Chinese-to-English translation using MarianMT. |
| [mbart-large-50-many-to-one-mmt](https://huggingface.co/facebook/mbart-large-50-many-to-one-mmt) | Multilingual Translation   | A multilingual model capable of translating from Chinese to English. |
| [nllb-200-zh-en](https://huggingface.co/facebook/nllb-200-zh-en)                                 | Neural Machine Translation | State-of-the-art multilingual translation model with high accuracy.  |

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

```bash
git clone https://github.com/xinihe/EnvInnovation_Agent.git
```

**2. Create a Virtual Environment**

```bash
python -m venv esg_venv
```

```bash
source esg_venv/bin/activate
```

**3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **Tutorial**

**Step 1: Summarize MDA Content**


**Step 2: Translate MDA Content**


**Step 3: Quantify Environmental Innovation**


**Step 4: Train a Custom LLM (Optional)**

### **References**
