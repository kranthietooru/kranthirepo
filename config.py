'''
    Config file has all Configuration settings to connect to Source and Target

'''
import os


###SQL Server_EDB Connection details
SQLSERVER_EDB_SERVER = 'padbs4101'
SQLSERVER_EDB_DATABASE = 'ENPRS_UNDG'
SQLSERVER_EDB_USERNAME = 'ZSOAUSRD'
SQLSERVER_EDB_PASSWORD = 'dNyAQHFet2ch4vKM'
SQLSERVER_EDB_DRIVER= '{ODBC Driver 13 for SQL Server}'

###SQL Server_PATH Connection details

SQLSERVER_PATH_SERVER = 'ZNDBCDD0937V'
SQLSERVER_PATH_DATABASE = 'PATH'
SQLSERVER_PATH_USERNAME = 'ZADERead'
SQLSERVER_PATH_PASSWORD = 'abc123'
SQLSERVER_PATH_DRIVER= '{ODBC Driver 13 for SQL Server}'

###SQL Server_Target Warehouse(MSTDB) Connection details
SQLSERVER_MSTDB_SERVER = 'datsqlsv01hub01dv01'
SQLSERVER_MSTDB_DATABASE = 'datsqlsv01hub01dv01'
SQLSERVER_MSTDB_USERNAME = 'sqladmin@datsqlsv01hub01dv01'
SQLSERVER_MSTDB_PASSWORD = 'sqSv1@Hub01!'
SQLSERVER_MSTDB_DRIVER= '{ODBC Driver 13 for SQL Server}'
SQLSERVER_MSTDB_ENCRYPT='yes'
SQLSERVER_MSTDB_TrustServerCertificate='no'
SQLSERVER_MSTDB_ConnectionTimeout='30'


###MY_SQL Connection Details

MY_SQL_SERVER = 'localhost'#'127.0.0.1:3306'
MY_SQL_DATABASE = 'SparkLoad'
MY_SQL_USERNAME = 'Spark'
MY_SQL_PASSWORD = 'Sparkpwd'
MY_SQL_DRIVER= 'pymysql.cursors.DictCursor'
MY_SQL_CHARACTERSET = 'utf8mb4'


### NETZZEA_ADS Connection Details
NETEZZA_ADS_SERVER = '10.147.163.19'
NETEZZA_ADS_DATABAE = 'ZNAWADSDBQ3'
NETEZZA_ADS_USERNAME = 'NZUSR'
NETEZZA_ADS_PASSWORD= 'znawlogin'
NETEZZA_ADS_DRIVER = '{NetezzaSQL}'
NETEZZA_ADS_PORT = '5480'

#### NETZZEA_MSTDB Connection Details 
#NETEZZA_MSTDB_SERVER = 'ZURNETCDCP12-FE'
#NETEZZA_MSTDB_DATABAE = 'ZEAMSTDBQ3'
#NETEZZA_MSTDB_USERNAME = 'NZUSR'
#NETEZZA_MSTDB_PASSWORD= 'znawlogin'
#NETEZZA_MSTDB_DRIVER = '{NetezzaSQL}'
#NETEZZA_MSTDB_PORT = '5480'

### NETEZZA_MSTDB ADE Connection Details
NETEZZA_MSTDB_SERVER = 'ZURNETCDCP12-FE'
NETEZZA_MSTDB_DATABAE = 'ZEAMSTDB_ADE'
NETEZZA_MSTDB_USERNAME = 'NZUSR'
NETEZZA_MSTDB_PASSWORD= 'znawlogin'
NETEZZA_MSTDB_DRIVER = '{NetezzaSQL}'
NETEZZA_MSTDB_PORT = '5480'

###NETZZEA_PMLHVADSDB Connection Details
NETEZZA_PMLHVADSDB_SERVER = 'zurnetcdcp12-fe'
NETEZZA_PMLHVADSDB_DATABAE = 'PMLHVADSQA'
NETEZZA_PMLHVADSDB_USERNAME = 'xcgpza1'
NETEZZA_PMLHVADSDB_PASSWORD= 'xcgpza1'
NETEZZA_PMLHVADSDB_DRIVER = '{NetezzaSQL}'
NETEZZA_PMLHVADSDB_PORT = '5480'

### DB2 Connection Details
DB2_SERVER = 'shaqin01'
DB2_DATABASE = 'EIDMODSQ'
DB2_USERNAME = 'INFAQADM'
DB2_PASSWORD = 'C3XKt8D67'
DB2_DRIVER = '{IBM DB2 ODBC DRIVER}'
DB2_PORT ='60134'

###SQL Server_RCIS Connection details

SQLSERVER_RCIS_SERVER = 'pdbisql05.corp.rcis.com'
SQLSERVER_RCIS_DATABASE = 'DM_ReinsuranceGroup'
SQLSERVER_RCIS_USERNAME = 'ganas01zna'
SQLSERVER_RCIS_PASSWORD = 'Monday#29'
SQLSERVER_RCIS_DRIVER= '{ODBC Driver 13 for SQL Server}'

### File Connection Details

RESULT_FILE_NAME = '\Result_File.csv'
SQLDATA_FILE_NAME = '\sqldata.csv'
STDOUT_File_NAME = '\stdout'
BLOBDT_FILENAME = '\\blobdt.csv'

LIST_OF_TABLES_PATH = "/".join(os.getcwd().strip("/").split('/')[:3]) + '\Scripts' ###'C:/Users/xcgkze1/Desktop/AdvocateTool_Zurich/CodeBaseVersion/'
LIST_OF_TABLES_FILE_NAME = '\Scripts\Table_name_list.csv'
RESULT_FOLDER_NAME = "/".join(os.getcwd().strip("/").split('/')[:3]) + '\Scripts' ###'C:/Users/xcgkze1/Desktop/AdvocateTool_Zurich/CodeBaseVersion/'
SOURCELOCALFILENAME = "/".join(os.getcwd().strip("/").split('/')[:3]) +'\Scripts\source'
LOCALFILENAME = "/".join(os.getcwd().strip("/").split('/')[:3]) + '\Scripts\stdout'

##Azure cloud conneciton details-for Hive Source-QA

SOURCEHIVESTORAGEACCTNAME = 'stor02spark36datahubqa01'
SOURCEHIVESTORAGEACCTKEY = 'l0NoGyih35Q7G7n3wnuhRe5oEH8vm7JkpSRvPa9Cj171Nfbcv8D73hMlT9WStRZ2eu6LIbdVIlTvVyBA+2rXdw=='
#'l0NoGyih35Q7G7n3wnuhRe5oEH8vm7JkpSRvPa9Cj171Nfbcv8D73hMlT9WStRZ2eu6LIbdVIlTvVyBA+2rXdw=='
SOURCEHIVESTORAGECONTNAME = 'ana02spark36datahubqa01'#'cont02spark36datahubqa01' #ana02spark36datahubqa01#
SOURCESTATUSDIR ='example/rest/AdvocateTool'
SOURCERESULTBLOBNAME= 'stdout'
SOURCEHIVEUSERNAME = "'advocate_qa'" # this vraible go into Poweshellscript hence we need to have double quotes and single quotes as well 
SOURCEHIVEPASSWORD = "'Welcome18'"# this vraible go into Poweshellscript hence we need to have double quotes and single quotes as well 
SOURCECLUSTERNAME = "'ana02spark36datahubqa01'"# this vraible go into Poweshellscript

HIVESTORAGEACCTNAME = 'stor02spark36datahubqa01'
HIVESTORAGEACCTKEY = 'l0NoGyih35Q7G7n3wnuhRe5oEH8vm7JkpSRvPa9Cj171Nfbcv8D73hMlT9WStRZ2eu6LIbdVIlTvVyBA+2rXdw=='
#'l0NoGyih35Q7G7n3wnuhRe5oEH8vm7JkpSRvPa9Cj171Nfbcv8D73hMlT9WStRZ2eu6LIbdVIlTvVyBA+2rXdw=='
HIVESTORAGECONTNAME = 'ana02spark36datahubqa01'#'cont02spark36datahubqa01' #ana02spark36datahubqa01#
STATUSDIR ='example/rest/AdvocateTool/VSTS'
RESULTBLOBNAME= 'stdout'
HIVEUSERNAME = "'advocate_qa'" # this vraible go into Poweshellscript hence we need to have double quotes and single quotes as well 
HIVEPASSWORD = "'Welcome18'"# this vraible go into Poweshellscript hence we need to have double quotes and single quotes as well 
CLUSTERNAME = "'ana02spark36datahubqa01'"# this vraible go into Poweshellscript


### Databricks Connection Details-Source
#DSN_SOURCE = 'MyAzureDatabricks_DSN' #QA Environment
DSN_SOURCE= 'MyAzureDatabricks_DSN_QA_1'   #Prod Environment
#DSN_SOURCE = 'MyAzureDatabricks_Dev_DSN' 

### Databricks Connection Details-Target
DSN_TARGET = 'MyAzureDatabricks_DSN_QA_1' #QA Environment
#DSN_TARGET = 'MyAzureDatabricks_DSN_Prod'   #Prod Environment
#DSN_TARGET = 'MyAzureDatabricks_Dev_DSN'


###RestAPI Variables
GetAPI = "https://znaopshub.visualstudio.com/DefaultCollection/_apis/projects"
RestUserName = ""
RestPassword = "goj2vkz6wyihbvgzs2zlk3encmtphyn7javjcteuvrymbjum37aq"
headers = {'content-type': 'application/json'}
ResultFileName= "Result_File.csv"
SqlDataFileName= "sqldata.csv"
