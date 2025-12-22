MODEL_NAME = "unsloth/Llama-3.2-1B-bnb-4bit"  ## 1Bパラメータ（超高速・軽量）
# その他の選択肢:
# "unsloth/Llama-3.2-3B-bnb-4bit"  ## 3Bパラメータ（バランス型）
# "unsloth/Qwen2.5-1.5B-bnb-4bit"  ## 1.5Bパラメータ（多言語対応）
DATASET_NAME = "shi3z/alpaca_cleaned_ja_json"

MAX_DATASET_SIZE = 500  ## データセットの最大サイズ
MAX_SEQ_LENGTH = 2048  ## シーケンス長
MAX_STEPS = 1  ## 学習ステップ数

# モデルの保存先ディレクトリ
MODEL_SAVE_DIR = "./rongocho_llm"
