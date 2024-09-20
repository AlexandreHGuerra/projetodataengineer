# Crie um arquivo chamado test_setup.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Conecte-se ao PostgreSQL
engine = create_engine('postgresql://postgres:mysecretpassword@localhost:6000/my_new_database')

# Crie um DataFrame simples
df = pd.DataFrame({
    'A': np.random.rand(10),
    'B': np.random.rand(10)
})

# Salve o DataFrame no PostgreSQL
df.to_sql('test_table', engine, if_exists='replace')

# Leia os dados de volta do PostgreSQL
df_from_db = pd.read_sql('test_table', engine)

# Plote os dados
df_from_db.plot(kind='bar')
plt.show()