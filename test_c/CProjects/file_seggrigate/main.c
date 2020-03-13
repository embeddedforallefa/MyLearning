#include <stdio.h>
#include <stdlib.h>

int Is_String_Present(char * str, char* search)
{
	int c1=0,c2=0,i,j,flg;

	while (str[c1]!='\0')
		c1++;
                c1--;

	while (search[c2]!='\0')
		c2++;
                c2--;


	for(i=0;i<=c1-c2;i++)
	{
		for(j=i;j<i+c2;j++)
		{
			flg=1;
			if (str[j]!=search[j-i])
			{
				flg=0;
			   break;
			}
		}
		if (flg==1)
			break;
	}
	if (flg==1)
		return 1;
	else
		return -1;
}

int main(void){
    char file_name[20];
    // read the string filename
    char baseFilename[105];
    int i=0;
    int j=0;
    int k=0;
    scanf("%[^\n]", baseFilename);
    FILE *fptr;
    FILE *fpc;
    FILE *fpcpp;
    FILE *fpcs;

    fpc = fopen("c_names_list_00.txt", "w");
    fpcpp = fopen("cpp_names_list_00.txt", "w");
    fpcs = fopen("cs_names_list_00.txt", "w");


    if ((fptr = fopen(baseFilename, "r")) == NULL){
        printf("Error opening file");
        /*Program exits if the file is not valid */
        exit(1);
    }
    else {
    printf("File opened correctly");
    }

      while(fgets(file_name, sizeof(file_name), fptr)){
        if (Is_String_Present(file_name, ".cs\n") == 1){
            //Write to cs_file
            //fputs(file_name, fpcs);
            printf("%s \n",file_name);
            fprintf(fpcs, file_name, k + 1);
            k++;
        }
    }
    // Read the text until the new line is encountered
    while(fgets(file_name, sizeof(file_name), fptr)){
        if(Is_String_Present(file_name, ".c\n") == 1){
            //Write to c_file
            //fputs(file_name, fpc);
            printf("%s \n",file_name);
            fprintf(fpc, file_name, i + 1);
            i++;
        }
        else{
            // Do nothing
        }
    }

    while(fgets(file_name, sizeof(file_name), fptr)){
        if(Is_String_Present(file_name, ".cpp\n") == 1){
            //Write to cpp_file
            //fputs(file_name, fpcpp);
            printf("%s \n",file_name);
            fprintf(fpcpp, file_name, j + 1);
            j++;
        }
    }

    fclose(fpc);
    fclose(fpcpp);
    fclose(fpcs);
    return 0;
}
