# AWS CloudFormation Template per go-to-live-kata

Questo template **AWS CloudFormation** permette di creare un'architettura ad alta disponibilità per il progetto "go-to-live-kata". L'architettura comprende una **VPC** con subnet pubbliche e private, un **bilanciamento del carico**, un **database RDS** e una **distribuzione CloudFront**.
## Architettura proposta

## Come Creare lo Stack
### Dalla Console AWS

1. Accedi alla tua console **AWS**.
2. Naviga su **AWS CloudFormation**.
3. Clicca su "**Create Stack**".
4. Seleziona "**Template is ready**" e "**Upload a template file**", quindi fai clic su "**Choose file**" per selezionare il tuo file `template CloudFormation.yaml` dal tuo computer.
5. Fai clic su "**Next**".
6. Compila i parametri richiesti".
7. Fai clic su "**Next**".
8. Fornisci un nome per lo stack, ad esempio "Prova".
9. Fai clic su "**Next**" e continua a completare il processo di creazione dello stack.

### Dalla AWS CLI

Assicurati di avere la **AWS CLI** installata e configurata sul tuo computer.

**Compila il file Parameters.json**  
Parameters.json è un file nella quale puoi andare a specificare i parametri che vuoi modificare , basta sostituire i ParameterValue relativi al parametro da inserire.

Lancia questo comando da terminale per creare lo stack
Sostituisci *NomeStack* con il nome dello stack che desideri impostare
```bash
aws cloudformation create-stack \
--stack-name NomeStack \
--template-body file://./template\ CloudFormation.yaml \
--parameters file://./Parameters.json
```
## Parametri del Template  
Il template richiede alcuni parametri per configurare correttamente l'architettura,altrimenti verranno messi di default.Assicurati di fornire i seguenti parametri:
* *VPCCIDR*: Il CIDR per la VPC
* *PrvSubnet1CIDR* e *PrvSubnet2CIDR*: CIDR per le subnet private.
* *PubSubnet1CIDR* e *PubSubnet2CIDR*: CIDR per le subnet pubbliche.
* *WPV*: La versione di WordPress da utilizzare.
* *DBMAZ*: Abilita o disabilita Multi-AZ per il database (true o false).
* *StorageDB*: Dimensione del disco del database.
* *DBNAME*: Nome del database di WordPress.
* *USERNAME* e *PASSWORD*: Credenziali di accesso DB per WordPress.
* *PriceClassCloudFront*: Classe di prezzo per CloudFront.

## Avvio dell'Architettura  
Dopo aver creato con successo lo stack, puoi accedere alla console AWS e iniziare a costruire il tuo progetto .

Ricorda di seguire le best practice per la sicurezza e di eliminare lo stack quando non ne hai più bisogno per evitare costi inutili.

## Risorse Aggiuntive

### Documentazione AWS

- [Documentazione AWS ufficiale](https://docs.aws.amazon.com/)

### Contatti

Per ulteriori domande o assistenza, puoi contattarci via email:

- Email: [matteo.lamalfa1108@gmail.com](mailto:tuo@email.com)
