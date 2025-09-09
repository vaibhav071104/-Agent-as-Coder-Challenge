[![Watch Demo](https://img.icons8.com/ios-filled/50/000000/video.png)](https://drive.google.com/file/d/16qQc0einQbawABXfZzyVCOI_0gk_BepV/view?usp=sharing)

# Agent-as-Coder Challenge

## Setup
1. pip install -r requirements.txt
2. Add PDF to data/icici/icic_sample.pdf
3. Add CSV to data/icici/result.csv
4. python agent.py --target icici
5. pytest tests/ -v

## Workflow

The Enhanced Bank Parser Agent follows a systematic autonomous workflow comprising five key stages: PLAN, OBSERVE, GENERATE, TEST, and SELF-DEBUG. Initially, in the PLAN phase, the agent formulates a strategic approach tailored for the target bank's document, specifying paths and parsing strategies. The OBSERVE phase involves analyzing the structure of input PDFs to extract representative sample data that informs subsequent code generation. During the GENERATE phase, the agent leverages advanced language models with multi-model fallback to produce custom parsing code, adhering to strict classification logic ensuring exactly one amount (debit or credit) per transaction. In the TEST phase, it validates the generated parser against expected outputs, checking schema compliance and classification accuracy. If errors are detected, the SELF-DEBUG phase iteratively refines the approach and regenerates code up to three attempts, resorting to a robust guaranteed fallback parser if necessary. This closed-loop automation ensures high accuracy, reliability, and robustness in bank statement parsing without human intervention.







