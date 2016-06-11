void setup() {
   Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
  
}

void loop() {
  
   String s = ""; //"740,1000 659,1000 587,1000 587,250 659,250 740,250 494,250 740,500 659,1000 587,250 659,250 740,1000 740,250 988,250 880,250 740,250 587,500 659,1000 370,250 494,250 587,1000 587,250 554,250 587,250 659,250 587,500 494,1000 440,250 494,250 554,500 554,250 587,250 554,500 494,250 440,250 494,200\n";
   do{
      s = Serial.readStringUntil('\n');
   }while(s == "");
   tocar(s.c_str());
   


}

void tocar(const char *notas){
       //char notas[] =  "740,1000 659,1000 587,1000 587,250 659,250 740,250 494,250 740,500 659,1000 587,250 659,250 740,1000 740,250 988,250 880,250 740,250 587,500 659,1000 370,250 494,250 587,1000 587,250 554,250 587,250 659,250 587,500 494,1000 440,250 494,250 554,500 554,250 587,250 554,500 494,250 440,250 494,200\n";
      //char notas[] =  "740,1000 659,1000\n";
      //printf("%s\n", notas);
      int l = strlen(notas);
      int i = 0; 
      int j;
      int indexComma = 0;
      int start = 0;
      for (i = 0; i < l; i++){
          char c = notas[i];
          if (c == ' ' || c == '\n' || c == '\0'){
              //printf("Start [%d]\n", start);
              //printf("Comma [%d]\n", indexComma);
              //printf("Space [%d]\n", i);
              int lnota = indexComma - start;
              char nota[lnota];
              int k = 0;
              for(j = start; j < indexComma; j++){
                  nota[k++] = notas[j];
              }
              nota[k] = '\0';
              //printf("[%s]\n", nota);
              //Serial.println(nota);
              
              int lduracao = i - indexComma;
              char duracao[lduracao];
              k = 0;
              for(j = indexComma+1; j < i; j++){
                  duracao[k++] = notas[j];
              }
              duracao[k] = '\0';
              //printf("[%s]\n", duracao);
              //Serial.println(duracao);
              
              int inota = atoi(nota);
              int iduracao = atoi(duracao);
              //tocarNota(atoi(nota), atoi(duracao));
              tone(10,inota, iduracao); 
              int pausaEntreNotas = iduracao;// * 1.30;
              delay(pausaEntreNotas);
              noTone(10);
              start = i+1;
          }else if (c == ','){
              indexComma = i;
          }
      }
  
}

