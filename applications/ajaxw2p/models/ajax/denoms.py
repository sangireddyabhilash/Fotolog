from gluon import dal
from storage import Storage

CONNECTION_STR = 'sqlite:://../databases/wave.db'
TWO_G_CHARGES_TABLE = 'two_g_charges'
THREE_G_CHARGES_TABLE = 'three_g_charges'
FULL_TALKTIME_CHARGES_TABLE = 'full_talktime_charges'
AMOUNT_COL = 'amount'

TWO_G_CHARGES_DATA_CSV_PATH = 'databases/2g_charges.csv'
THREE_G_CHARGES_DATA_CSV_PATH = 'databases/3g_charges.csv'
FULL_TALKTIME_CHARGES_DATA_CSV_PATH = 'databases/full_talktime_charges.csv'

def readTable(db, table):
    denominations = []
    rows = db(table).select()
    if len(rows) > 0:
        rowsAmount = db(table.amount).select(table.amount)
        for row in rowsAmount:
            denominations.append(int(row.amount))

    return denominations

def get2GCharges():
    global CONNECTION_STR, TWO_G_CHARGES_TABLE, AMOUNT_COL
    db = dal.DAL(uri=CONNECTION_STR,  migrate=False)
    field = db.Field(AMOUNT_COL, type='integer', required=True, notnull=True, unique=True)
    table = db.define_table(TWO_G_CHARGES_TABLE, field, redefine=False)
    return readTable(db, table)

def get3GCharges():
    global CONNECTION_STR, THREE_G_CHARGES_TABLE, AMOUNT_COL
    db = dal.DAL(uri=CONNECTION_STR,  migrate=False)
    field = db.Field(AMOUNT_COL, type='integer', required=True, notnull=True, unique=True)
    table = db.define_table(THREE_G_CHARGES_TABLE, field, redefine=False)
    return readTable(db, table)

def getFullTalktimeCharges():
    global CONNECTION_STR, FULL_TALKTIME_CHARGES_TABLE, AMOUNT_COL
    db = dal.DAL(uri=CONNECTION_STR,  migrate=False)
    field = db.Field(AMOUNT_COL, type='integer', required=True, notnull=True, unique=True)
    table = db.define_table(FULL_TALKTIME_CHARGES_TABLE, field, redefine=False)
    return readTable(db, table)

###############################################################################

def getDenominations():
  args = request.args
  #if args[0] == '2g':
  #  response.denominations2G = get2GCharges()
  if len(args) is 0:
    plan = '2g'
  else:
    plan = args[0].lower()

  if plan == '2g':
    response.denominations2G = get2GCharges()
  elif plan == '3g':
    response.denominations3G = get3GCharges()
  else:
    response.denominationsFullTalktime = getFullTalktimeCharges()

getDenominations()

