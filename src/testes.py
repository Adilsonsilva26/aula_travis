importação  jogovelha
 sys de importação

erroInicializar  =  False
jogo  =  jogovelha . inicializar ()

se  len ( jogo ) ! =  3 :
    erroInicializar  =  True
mais :
   para  linha  in  jogo :
        se  len ( linha ) ! =  3 :
                  erroInicializar  =  True
        mais :
                  para  elemento  em  linha :
                      if  elemento  ! =  '.' :
                          erroInicializar  =  True
                          if  erroInicializar :
                             sys . saída ( 1 )
                          mais :
                             sys . saída ( 0 )
