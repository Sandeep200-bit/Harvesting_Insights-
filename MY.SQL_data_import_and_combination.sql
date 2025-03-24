use india_agricultural_datasets;

select * from apples ;



CREATE TABLE crops_master (
    Domain_Code VARCHAR(10),
    Domain VARCHAR(100),
    Area_Code INT,
    Area VARCHAR(100),
    Element_Code INT,
    Element VARCHAR(100),
    Item_Code INT,
    Item VARCHAR(100),
    Year_Code INT,
    Year INT,
    Unit VARCHAR(20),
    Value FLOAT,
    Flag VARCHAR(10),
    Flag_Description VARCHAR(100)
);

select * from crops_master ;


INSERT INTO crops_master
SELECT * FROM apples
UNION ALL 
SELECT * FROM apricots
UNION ALL 
SELECT * FROM areca_nuts
UNION ALL 
SELECT * FROM bananas
UNION ALL 
SELECT * FROM barley
UNION ALL 
SELECT * FROM beans_dry
UNION ALL 
SELECT * FROM beans_green
UNION ALL 
SELECT * FROM cabbage
UNION ALL 
SELECT * FROM carrots
UNION ALL 
SELECT * FROM cashewnuts
UNION ALL 
SELECT * FROM cauliflower
UNION ALL 
SELECT * FROM cherries
UNION ALL 
SELECT * FROM chilli_dry
UNION ALL 
SELECT * FROM chilli_green
UNION ALL 
SELECT * FROM coconuts
UNION ALL 
SELECT * FROM coffee
UNION ALL 
SELECT * FROM cucumber
UNION ALL 
SELECT * FROM eggplant
UNION ALL 
SELECT * FROM fennel_coriander
UNION ALL 
SELECT * FROM garlic
UNION ALL 
SELECT * FROM ginger
UNION ALL 
SELECT * FROM grapes
UNION ALL 
SELECT * FROM lemons
UNION ALL 
SELECT * FROM groundnuts
UNION ALL 
SELECT * FROM lentils
UNION ALL 
SELECT * FROM lettuce
UNION ALL 
SELECT * FROM maize
UNION ALL 
SELECT * FROM mangoes
UNION ALL 
SELECT * FROM melons
UNION ALL 
SELECT * FROM okra
UNION ALL 
SELECT * FROM nutmeg
UNION ALL 
SELECT * FROM onions
UNION ALL 
SELECT * FROM papaya
UNION ALL 
SELECT * FROM oranges
UNION ALL 
SELECT * FROM peaches
UNION ALL 
SELECT * FROM peas
UNION ALL 
SELECT * FROM pears
UNION ALL 
SELECT * FROM pepper
UNION ALL 
SELECT * FROM pineapples
UNION ALL 
SELECT * FROM potatoes
UNION ALL 
SELECT * FROM pumpkins
UNION ALL 
SELECT * FROM rice
UNION ALL 
SELECT * FROM safflower
UNION ALL 
SELECT * FROM sugarcane
UNION ALL 
SELECT * FROM soyabean
UNION ALL 
SELECT * FROM sesame
UNION ALL  
SELECT * FROM tomatoes
UNION ALL 
SELECT * FROM watermelon
UNION ALL 
SELECT * FROM wheat;


select * from crops_master ;


select * from temperature ; 

select * from rainfall ;
























































































































