//+------------------------------------------------------------------+
//|                                                   WebRequest.mq4 |
//|                                Copyright 2020, Pearlock pvt.Ltd. |
//|                                             https://www.mql5.com |
//+------------------------------------------------------------------+
#property copyright "Copyright 2020, Pearlock pvt.Ltd."
#property link      "https://www.mql5.com"
#property version   "1.00"
#property strict

input string url = "https://veeresh-ps.000webhostapp.com/2183";
string InpFileName="licence.txt"; // file name
string InpDirectoryName=TerminalInfoString(TERMINAL_COMMONDATA_PATH); // directory name
int licence_len=10;

bool enable_EA=false;
bool Work=false;                    // EA will work.
bool licence_valid = false;                
//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int OnInit()
  {
   string licence_local;
   string headers;
   char post[], result[];
   int res;

   ResetLastError();
   int filehandle_local = FileOpen(InpFileName,FILE_READ|FILE_TXT|FILE_ANSI);
   
      if(filehandle_local!=INVALID_HANDLE)
     {
      PrintFormat("%s file is available for reading",InpFileName);
      PrintFormat("File path: %s\\Files\\",TerminalInfoString(TERMINAL_DATA_PATH));
      //--- read data from the file
      while(!FileIsEnding(filehandle_local))
        {
         //--- read the licence string
         licence_local=FileReadString(filehandle_local);
        }
      //--- close the file
      FileClose(filehandle_local);
      PrintFormat("Data is read, %s file is closed",InpFileName);
     }
   else
      PrintFormat("Failed to open %s file, Error code = %d",InpFileName,GetLastError());
      
   res = WebRequest("GET", url, NULL, NULL, 5000, post, 0, result, headers);

   if(res == -1)
     {
      Print("request did not successeed :", GetLastError());
      MessageBox("you want to connect to" + url + "and error is", MB_ICONINFORMATION);
     }
   else
     {
      PrintFormat("the resulting array size is: %d ",ArraySize(result));
      for(int i=0; i < licence_len; i++)
           {
            Print(result[i]);
            Print(licence_local[i]);
            Print("*******");
            if((i%2)==0)
            {
               if(result[i]==licence_local[i]+1)
               {
                  licence_valid = true;
               }
               else
               {
                  licence_valid = false;
               }
            }
            else
            {
               if(result[i]==licence_local[i]-1)
               {
                  licence_valid = true;
               }
               else
               {
                  licence_valid = false;
               }
            }
           }
     }
     
     if(licence_valid ==true)
     {
      Print("License is valid");
      enable_EA=true;
     }
     else
     {
      enable_EA=false;
      Print("You do not have a valid licece : Contact Team Pearlock");
     }
   return(INIT_SUCCEEDED);
  }
//+------------------------------------------------------------------+
//| Expert deinitialization function                                 |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {
  }
//+------------------------------------------------------------------+
//| Expert tick function                                             |
//+------------------------------------------------------------------+
void OnTick()
  {

//---
if(enable_EA==true)
  {
   PrintFormat("You do have a valid licece");
  }
  else
  {
   PrintFormat("You do not have a valid licece : Contact Team Pearlock");
  }
  }
//+------------------------------------------------------------------+
//| Timer function                                                   |
//+------------------------------------------------------------------+
void OnTimer()
  {
//---

  }
//+------------------------------------------------------------------+
//| Tester function                                                  |
//+------------------------------------------------------------------+
double OnTester()
  {
//---
   double ret=0.0;
//---

//---
   return(ret);
  }
//+------------------------------------------------------------------+
//| ChartEvent function                                              |
//+------------------------------------------------------------------+
void OnChartEvent(const int id,
                  const long &lparam,
                  const double &dparam,
                  const string &sparam)
  {
//---

  }
//+------------------------------------------------------------------+
