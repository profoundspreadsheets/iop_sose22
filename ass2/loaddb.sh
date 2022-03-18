echo "dropping tables"
psql -d iop -U paul < drop.sql
echo "creating tables"
psql -d iop -U paul < create.sql
source ~/miniconda3/etc/profile.d/conda.sh
echo "activating python env"
conda activate iop
echo "installing requirements"
conda install --file code/requirements.txt
cd code
echo "filling databases"
python main.py