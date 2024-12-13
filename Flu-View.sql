CREATE TABLE "flu_data_by_state" (
    "id" int   NOT NULL,PRIMARY KEY
    "REGION" VARCHAR   NOT NULL,
    "YEAR" INTEGER   NOT NULL,
    "WEEK" INTEGER   NOT NULL,
    "ILITOTAL" DECIMAL   NOT NULL,
    "STATE_ABBR" VARCHAR   NOT NULL,
    
     
);

CREATE TABLE "AgeViewBySeason" (
    "id" INTEGER   NOT NULL,PRIMARY KEY
    "Season" vARCHAR(50)   NOT NULL,
    "Age_Group" VARCHAR(50)   NOT NULL,
    "A(H1)" INTEGER   NOT NULL,
    "A(Unable_to_subtype)" INTEGER   NOT NULL,
    "A(H3)" INTEGER   NOT NULL,
    "A(H1N1)pdm09" INTEGER   NOT NULL,
    "A(subtyping_not_performed)" INTEGER   NOT NULL,
    "B(Vivtoria_Lineage)" INTEGER   NOT NULL,
    "B(Yamagata_Lineage)" INTEGER   NOT NULL,
    "B(Lineage_Unspecified)" INTEGER   NOT NULL,
    "H3N2v" INTEGER   NOT NULL,
    
     
);
CREATE TABLE "STATE_ACTIVITY_LEVEL" (
    "id" INTEGER   NOT NULL,pRIMARY KEY
    "STATENAME" VARCHAR   NOT NULL,
    "ACTIVITY_LEVEL" VARCHAR(50)   NOT NULL,
    "WEEK" INTEGER   NOT NULL,
    "SEASON" VARCHAR(50)   NOT NULL,
    
     
);

CREATE TABLE "Mortality_Data" (
    "id" int   NOT NULL,PRIMARY KEY
    
    "WEEK" INTEGER   NOT NULL,
    "INFLUENZA_DEATHS" INTEGER   NOT NULL,
    "TOTAL_DEATHS" INTEGER   NOT NULL,
    
);