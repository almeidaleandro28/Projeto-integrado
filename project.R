library(ggplot2)
library(dplyr)

df = read.table('datatran2024.csv', header = TRUE,  sep = ';',  stringsAsFactors = FALSE)

# headData <- head( df )
# summaryData <- summary( df )
# strData <- str( df )
# colnamesData <- colnames( df )

#-------------------------------------
#1 - identificar as principais causas e condições associadas a acidentes graves e fatais
causaAcidentes <- df['causa_acidente']
causaAcidentesCount <- table( causaAcidentes)
causaAcidentesOrder <- sort( causaAcidentesCount )
causaAcidentesUnique <- unique( causaAcidentes )

classificacaoAcidentes <- df['classificacao_acidente']
classificacaooAcidentesCount <- table( tiposAcidentes )

mortos <- df['mortos']
feridoGraves <- df['feridos_graves']



pg <- ggplot( df , aes(x = causa_acidente )) +
  geom_bar(fill = "steelblue") +
  labs(title = "Tipos de Acidentes", x = "Tipo de Acidente", y = "Frequência") +
  theme_minimal()


topCauses <- top_causes <- df %>%
  count( causa_acidente , sort = TRUE) %>%
  top_n(15, n)

print( feridoGraves )
