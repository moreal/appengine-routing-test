cd $1

virtualenv env -p python
source env/bin/activate
pip install -t lib -r requirements.txt

yes | gcloud app deploy --project path-routing-test

deactivate

cd -