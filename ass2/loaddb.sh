psql -d iop -U paul < drop.sql
psql -d iop -U paul < create.sql
source ~/miniconda3/etc/profile.d/conda.sh
conda activate iop
cd code
python main.py