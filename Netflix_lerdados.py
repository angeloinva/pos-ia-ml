{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ea93bd37-bd5f-46ab-adac-76e34e2fc361",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "fa9aca72-bb27-4c9e-9fad-e0358b95579d",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'data/netflix_titles.csv'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mFileNotFoundError\u001b[39m                         Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[4]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[32m      1\u001b[39m filename = \u001b[33m'\u001b[39m\u001b[33mdata/netflix_titles.csv\u001b[39m\u001b[33m'\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m df = pd.read_csv(filename, parse_dates=[\u001b[33m'\u001b[39m\u001b[33mdate_added\u001b[39m\u001b[33m'\u001b[39m])\n\u001b[32m      3\u001b[39m df.head()\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\pandas\\io\\parsers\\readers.py:1026\u001b[39m, in \u001b[36mread_csv\u001b[39m\u001b[34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, date_format, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, on_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options, dtype_backend)\u001b[39m\n\u001b[32m   1013\u001b[39m kwds_defaults = _refine_defaults_read(\n\u001b[32m   1014\u001b[39m     dialect,\n\u001b[32m   1015\u001b[39m     delimiter,\n\u001b[32m   (...)\u001b[39m\u001b[32m   1022\u001b[39m     dtype_backend=dtype_backend,\n\u001b[32m   1023\u001b[39m )\n\u001b[32m   1024\u001b[39m kwds.update(kwds_defaults)\n\u001b[32m-> \u001b[39m\u001b[32m1026\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m _read(filepath_or_buffer, kwds)\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\pandas\\io\\parsers\\readers.py:620\u001b[39m, in \u001b[36m_read\u001b[39m\u001b[34m(filepath_or_buffer, kwds)\u001b[39m\n\u001b[32m    617\u001b[39m _validate_names(kwds.get(\u001b[33m\"\u001b[39m\u001b[33mnames\u001b[39m\u001b[33m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m))\n\u001b[32m    619\u001b[39m \u001b[38;5;66;03m# Create the parser.\u001b[39;00m\n\u001b[32m--> \u001b[39m\u001b[32m620\u001b[39m parser = TextFileReader(filepath_or_buffer, **kwds)\n\u001b[32m    622\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m chunksize \u001b[38;5;129;01mor\u001b[39;00m iterator:\n\u001b[32m    623\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m parser\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\pandas\\io\\parsers\\readers.py:1620\u001b[39m, in \u001b[36mTextFileReader.__init__\u001b[39m\u001b[34m(self, f, engine, **kwds)\u001b[39m\n\u001b[32m   1617\u001b[39m     \u001b[38;5;28mself\u001b[39m.options[\u001b[33m\"\u001b[39m\u001b[33mhas_index_names\u001b[39m\u001b[33m\"\u001b[39m] = kwds[\u001b[33m\"\u001b[39m\u001b[33mhas_index_names\u001b[39m\u001b[33m\"\u001b[39m]\n\u001b[32m   1619\u001b[39m \u001b[38;5;28mself\u001b[39m.handles: IOHandles | \u001b[38;5;28;01mNone\u001b[39;00m = \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[32m-> \u001b[39m\u001b[32m1620\u001b[39m \u001b[38;5;28mself\u001b[39m._engine = \u001b[38;5;28mself\u001b[39m._make_engine(f, \u001b[38;5;28mself\u001b[39m.engine)\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\pandas\\io\\parsers\\readers.py:1880\u001b[39m, in \u001b[36mTextFileReader._make_engine\u001b[39m\u001b[34m(self, f, engine)\u001b[39m\n\u001b[32m   1878\u001b[39m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[33m\"\u001b[39m\u001b[33mb\u001b[39m\u001b[33m\"\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m mode:\n\u001b[32m   1879\u001b[39m         mode += \u001b[33m\"\u001b[39m\u001b[33mb\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m-> \u001b[39m\u001b[32m1880\u001b[39m \u001b[38;5;28mself\u001b[39m.handles = get_handle(\n\u001b[32m   1881\u001b[39m     f,\n\u001b[32m   1882\u001b[39m     mode,\n\u001b[32m   1883\u001b[39m     encoding=\u001b[38;5;28mself\u001b[39m.options.get(\u001b[33m\"\u001b[39m\u001b[33mencoding\u001b[39m\u001b[33m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m),\n\u001b[32m   1884\u001b[39m     compression=\u001b[38;5;28mself\u001b[39m.options.get(\u001b[33m\"\u001b[39m\u001b[33mcompression\u001b[39m\u001b[33m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m),\n\u001b[32m   1885\u001b[39m     memory_map=\u001b[38;5;28mself\u001b[39m.options.get(\u001b[33m\"\u001b[39m\u001b[33mmemory_map\u001b[39m\u001b[33m\"\u001b[39m, \u001b[38;5;28;01mFalse\u001b[39;00m),\n\u001b[32m   1886\u001b[39m     is_text=is_text,\n\u001b[32m   1887\u001b[39m     errors=\u001b[38;5;28mself\u001b[39m.options.get(\u001b[33m\"\u001b[39m\u001b[33mencoding_errors\u001b[39m\u001b[33m\"\u001b[39m, \u001b[33m\"\u001b[39m\u001b[33mstrict\u001b[39m\u001b[33m\"\u001b[39m),\n\u001b[32m   1888\u001b[39m     storage_options=\u001b[38;5;28mself\u001b[39m.options.get(\u001b[33m\"\u001b[39m\u001b[33mstorage_options\u001b[39m\u001b[33m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m),\n\u001b[32m   1889\u001b[39m )\n\u001b[32m   1890\u001b[39m \u001b[38;5;28;01massert\u001b[39;00m \u001b[38;5;28mself\u001b[39m.handles \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[32m   1891\u001b[39m f = \u001b[38;5;28mself\u001b[39m.handles.handle\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\pandas\\io\\common.py:873\u001b[39m, in \u001b[36mget_handle\u001b[39m\u001b[34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001b[39m\n\u001b[32m    868\u001b[39m \u001b[38;5;28;01melif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(handle, \u001b[38;5;28mstr\u001b[39m):\n\u001b[32m    869\u001b[39m     \u001b[38;5;66;03m# Check whether the filename is to be opened in binary mode.\u001b[39;00m\n\u001b[32m    870\u001b[39m     \u001b[38;5;66;03m# Binary mode does not support 'encoding' and 'newline'.\u001b[39;00m\n\u001b[32m    871\u001b[39m     \u001b[38;5;28;01mif\u001b[39;00m ioargs.encoding \u001b[38;5;129;01mand\u001b[39;00m \u001b[33m\"\u001b[39m\u001b[33mb\u001b[39m\u001b[33m\"\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m ioargs.mode:\n\u001b[32m    872\u001b[39m         \u001b[38;5;66;03m# Encoding\u001b[39;00m\n\u001b[32m--> \u001b[39m\u001b[32m873\u001b[39m         handle = \u001b[38;5;28mopen\u001b[39m(\n\u001b[32m    874\u001b[39m             handle,\n\u001b[32m    875\u001b[39m             ioargs.mode,\n\u001b[32m    876\u001b[39m             encoding=ioargs.encoding,\n\u001b[32m    877\u001b[39m             errors=errors,\n\u001b[32m    878\u001b[39m             newline=\u001b[33m\"\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m    879\u001b[39m         )\n\u001b[32m    880\u001b[39m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[32m    881\u001b[39m         \u001b[38;5;66;03m# Binary mode\u001b[39;00m\n\u001b[32m    882\u001b[39m         handle = \u001b[38;5;28mopen\u001b[39m(handle, ioargs.mode)\n",
      "\u001b[31mFileNotFoundError\u001b[39m: [Errno 2] No such file or directory: 'data/netflix_titles.csv'"
     ]
    }
   ],
   "source": [
    "filename = 'data/netflix_titles.csv'\n",
    "df = pd.read_csv(filename, parse_dates=['date_added'])\n",
    "df.head()       "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a102dcb7-a1f9-41d6-9720-eaf25ae961b3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
