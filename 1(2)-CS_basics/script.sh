# anaconda(또는 miniconda)가 존재하지 않을 경우 설치해주세요!
MINICONDA_DIR="$HOME/miniconda"
if [ -d "$MINICONDA_DIR" ]; then 
  export PATH="$MINICONDA_DIR/bin:$PATH"
fi

if ! command -v conda &> /dev/null; then
  echo "[INFO] conda 없어서 설치 중..."
  # 리눅스용 Miniconda 설치 스크립트 다운로드
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
  bash miniconda.sh -b -p "$MINICONDA_DIR"
  rm miniconda.sh
  export PATH="$MINICONDA_DIR/bin:$PATH"
fi


# Conda 환셩 생성 및 활성화
if ! conda env list | grep -q "^myenv"; then
  conda create -y -n myenv python=3.10
fi

# activate
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate myenv

## 건드리지 마세요! ##
python_env=$(python -c "import sys; print(sys.prefix)")
if [[ "$python_env" == *"/envs/myenv"* ]]; then
    echo "[INFO] 가상환경 활성화: 성공"
else
    echo "[INFO] 가상환경 활성화: 실패"
    exit 1 
fi

# 필요한 패키지 설치
pip install mypy

# Submission 폴더 파일 실행
cd ../1\(1\)-Python/submission || { echo "[INFO] submission 디렉토리로 이동 실패"; exit 1; }

for file in *.py; do
  base="${file%.py}" # 파일명에서 확장자 뗀 이름 얻기
  prob="${base#*_}" #언더바 잘라내고 순수 문제번호만 추출
  python "$file" < "../../1(2)-CS_basics/input/${prob}_input" \
                 >   "../../1(2)-CS_basics/output/${prob}_output"
    echo "[INFO] $file 실행 완료 → output/${prob}_output"
done

# mypy 테스트 실행 및 mypy_log.txt 저장
mypy . > "../../1(2)-CS_basics/mypy_log.txt" 2>&1
echo "[INFO] mypy 검사 완료 → mypy_log.txt"

# conda.yml 파일 생성
conda env export -n myenv --no-builds \
  > "../../1(2)-CS_basics/conda.yml"
echo "[INFO] conda 환경 내보내기 완료 → conda.yml"

# 가상환경 비활성화
conda deactivate
echo "[INFO] 가상환경 비활성화"