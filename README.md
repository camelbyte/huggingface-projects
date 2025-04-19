# 🤗 Hugging Face NLP Project: Data Analysis - Polling

> A reproducible pipeline leveraging Hugging Face Transformers and Datasets for classficication and analysis. 

---

## 📌 Project Overview

This project demonstrates how to use Hugging Face's `transformers`, `datasets`, and `huggingface_hub` libraries to:
- Load and preprocess data (from Hugging Face Hub or external sources)
- Run inference using pretrained models
- (Optional) Fine-tune models on custom datasets
- (Optional) Deploy pipelines or agents for production

---

## 🧠 Key Features

- ✅ Uses pretrained models from 🤗 Transformers Hub
- ✅ Supports inference pipelines (`sentiment-analysis`, `summarization`, etc.)
- ✅ Integrates with `datasets` for scalable evaluation
- ✅ Model outputs saved in `.csv` or `.jsonl`
- ✅ Modular and extensible pipeline architecture

---

## 📁 Project Structure

```bash
.
├── get_data.py           # Downloads or loads dataset
├── run_inference.py      # Runs HF pipeline over dataset
├── analyze_results.py    # Optional: postprocessing/plotting
├── model_config.json     # Model-specific parameters (optional)
├── requirements.txt
└── README.md
****
