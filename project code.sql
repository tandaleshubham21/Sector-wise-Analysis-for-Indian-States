SELECT * FROM project.sectoral_analysis;

select * from project.sectoral_analysis where StateName="Maharashtra";

select DistName from project.sectoral_analysis where StateName="Maharashtra" and Year=2008 and `TotalCurrentPrices(inMillionsRs)` > 100000;

select sum(`PRIMARYSECTORCONSTANTPRICES(inMillionsRs)` + `PRIMARYSECTORCURRENTPRICES(inMillionRs)`) as total_contribution_of_primary_sector from project.sectoral_analysis where StateName="Maharashtra" and Year=2008;

select ds1.StateName, sum(distinct ds1.`TotalConstantPrices(inMillionsRs)` + ds1.`TotalCurrentPrices(inMillionsRs)`) as total_contribution, count(distinct ds1.DistName) as number_of_district from sectoral_analysis ds1 join sectoral_analysis ds2 
on ds1.StateCode=ds2.StateCode group by ds1.StateName;

select ds1.Year as years, ds1.`SECONDARYSECTORCURRENTPRICES(MillionsinRs)` as current_values, ds2.`SECONDARYSECTORCURRENTPRICES(MillionsinRs)` as previous_value, (ds1.`SECONDARYSECTORCURRENTPRICES(MillionsinRs)`-ds2.`SECONDARYSECTORCURRENTPRICES(MillionsinRs)`)/ds2.`SECONDARYSECTORCURRENTPRICES(MillionsinRs)` * 100 as yr_on_yr_growth from sectoral_analysis ds1 join sectoral_analysis ds2 
on ds1.DistName=ds2.DistName and ds1.Year=ds2.Year+1 where ds1.DistName="Thane";

select DistName, (max(`TERTIARYSECTORCURRENTPRICES(MillionsinRs)`)-min(`TERTIARYSECTORCURRENTPRICES(MillionsinRs)`))/min(`TERTIARYSECTORCURRENTPRICES(MillionsinRs)`)*100 as growth_rate from project.sectoral_analysis where Year in(2007,2008,2009,2010,2011)
group by DistName order by growth_rate desc limit 1;

select StateName, sum(`SECONDARYSECTORCONSTANTPRICES(MillionsinRs)`) as total_secondary_sector_contribution from project.sectoral_analysis group by StateName;

select DistName, `PerCapitaCurrentPrices(1000inRs)` from project.sectoral_analysis where (DistName="Thane" or DistName="Raigad") and Year=2008;

select DistName, StateName, Year, `TotalConstantPrices(inMillionsRs)`, rank() over(partition by StateName order by `TotalConstantPrices(inMillionsRs)` desc) as ranks from project.sectoral_analysis where StateName="Maharashtra" and Year=2008;

select DistName, Year, `PRIMARYSECTORCONSTANTSHARES(Percent)` from project.sectoral_analysis where StateName="Maharashtra" and `PRIMARYSECTORCONSTANTSHARES(Percent)`>20 and Year=(select max(Year) from project.sectoral_analysis);

select StateName, avg(`TERTIARYSECTORCURRENTSHARES(Percent)`) as avg_tertiary_shares from project.sectoral_analysis group by StateName;

select StateName, DistName, Year, `TotalCurrentPrices(inMillionsRs)` as max_total_current_prices from project.sectoral_analysis where Year=2008 and StateName="Maharashtra" and `TotalCurrentPrices(inMillionsRs)`=(select max(`TotalCurrentPrices(inMillionsRs)`) from project.sectoral_analysis where Year=2008 and StateName="Maharashtra");

select StateName, DistName, Year, `TotalCurrentPrices(inMillionsRs)` as min_total_current_prices from project.sectoral_analysis where Year=2008 and StateName="Maharashtra" and `TotalCurrentPrices(inMillionsRs)`=(select min(`TotalCurrentPrices(inMillionsRs)`) from project.sectoral_analysis where Year=2008 and StateName="Maharashtra");

select DistName, (sum(`SECONDARYSECTORCURRENTPRICES(MillionsinRs)`)/sum(`TotalCurrentPrices(inMillionsRs)`))*100 as secondary_sector_contribution_percentage from project.sectoral_analysis where StateName="Maharashtra" group by DistName;

select DistName, Year, `TERTIARYSECTORCONSTANTSHARES(Percent)`, `SECONDARYSECTORCONSTANTSHARES(Percent)` from project.sectoral_analysis where StateName="Maharashtra" and Year=2008 and `TERTIARYSECTORCONSTANTSHARES(Percent)`>`SECONDARYSECTORCONSTANTSHARES(Percent)`;

select DistName, `PRIMARYSECTORCONSTANTSHARES(Percent)`, `SECONDARYSECTORCONSTANTSHARES(Percent)` from project.sectoral_analysis where StateName="Maharashtra" and `PRIMARYSECTORCONSTANTSHARES(Percent)`>30 and `SECONDARYSECTORCONSTANTSHARES(Percent)`>30;

select Year, DistName, `TotalCurrentPrices(inMillionsRs)` from project.sectoral_analysis where DistName="Thane" order by Year asc;

select StateName, Year, sum(`TERTIARYSECTORCURRENTPRICES(MillionsinRs)`) as total_tertiary_sector_contribution from project.sectoral_analysis where Year=2008 group by StateName
having total_tertiary_sector_contribution=(select max(total_tertiary_sector) from (select StateName, sum(`TERTIARYSECTORCURRENTPRICES(MillionsinRs)`) as total_tertiary_sector from project.sectoral_analysis where Year=2008 group by StateName) as state_tertiary_totals);

select distinct StateName from project.sectoral_analysis;

select StateName, DistName, Year, sum(`TotalCurrentPrices(inMillionsRs)`) as total_economic_contribution from project.sectoral_analysis where StateName="Maharashtra" and Year=2008 group by DistName;

select Year, DistName, `PRIMARYSECTORCONSTANTPRICES(inMillionsRs)`, sum(`PRIMARYSECTORCONSTANTPRICES(inMillionsRs)`) over(partition by DistName order by Year) as cumulative_primary_sector from project.sectoral_analysis where DistName="Thane" order by Year;