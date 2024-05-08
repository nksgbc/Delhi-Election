{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'mysql'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mmysql\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mconnector\u001b[39;00m \n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m      4\u001b[0m     \u001b[38;5;66;03m# Connect to the MySQL server\u001b[39;00m\n\u001b[0;32m      5\u001b[0m     connection \u001b[38;5;241m=\u001b[39m mysql\u001b[38;5;241m.\u001b[39mconnector\u001b[38;5;241m.\u001b[39mconnect(\n\u001b[0;32m      6\u001b[0m         host\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mlocalhost\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m      7\u001b[0m         user\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mroot\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m      8\u001b[0m         password\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mMySQL98\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m      9\u001b[0m         database\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdelhielection\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     10\u001b[0m     )\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'mysql'"
     ]
    }
   ],
   "source": [
    "import mysql.connector \n",
    "\n",
    "try:\n",
    "    # Connect to the MySQL server\n",
    "    connection = mysql.connector.connect(\n",
    "        host=\"localhost\",\n",
    "        user=\"root\",\n",
    "        password=\"MySQL98\",\n",
    "        database=\"delhielection\"\n",
    "    )\n",
    "\n",
    "    if connection.is_connected():\n",
    "        print('Connected to MySQL database')\n",
    "\n",
    "except mysql.connector.Error as error:\n",
    "    print(f'Error connecting to MySQL database: {error}')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
