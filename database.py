from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/flaskproject?charset=utf8mb4", connect_args={"ssl_disabled": True})

    # print(type(result))

    # result_all = result.all()

    # print(type(result_all))

    # first_row = result_all[0]

    # convert_dict = dict(first_row._mapping)

    # print(type(convert_dict))

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))

    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs
  
def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {'val':id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0]._mapping)