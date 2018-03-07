import React from 'react';
import { VictoryBar, VictoryChart,
  VictoryScatter,VictoryTheme,
  VictoryAxis } from 'victory';

function makeVitaminData(props) {
  const vitaminData = [];
  vitaminData.push({x : "A (IU)", y: props.data["vitamin_a"]});
  vitaminData.push({x : "C (IU)", y: props.data["vitamin_c"]});
  vitaminData.push({x : "D (IU)", y: props.data["vitamin_d"]});
  vitaminData.push({x : "B12 (mcg)", y: props.data["vitamin_b12"]});
  return vitaminData;
}

function makekCalData(props) {
  const kcalData = [];
  const protein = props.data["protein"];
  const carbs = props.data["carbohydrates"];
  const fat = props.data["fat"];
  const totalGrams = protein + carbs + fat;
  const totalkCal = props.data["kcal"];
  kcalData.push({x: "protein", y : Math.floor((protein / totalGrams) * totalkCal)  });
  kcalData.push({x: "carbs", y : Math.floor((carbs / totalGrams) * totalkCal)});
  kcalData.push({x: "fat", y : Math.floor((fat / totalGrams) * totalkCal)});
  return kcalData;
}

function makeMineralData(props) {
  const mineralData = [];
  const calcium = props.data["calcium"];
  const iron = props.data["iron"];
  const magnesium = props.data["magnesium"];
  const potassium = props.data["potassium"];
  const sodium = props.data["sodium"];
  const zinc = props.data["zinc"];
  mineralData.push({x : "Ca", y : calcium});
  mineralData.push({x : "Fe", y : iron});
  mineralData.push({x : "Mg", y : magnesium});
  mineralData.push({x : "K", y : potassium});
  mineralData.push({x : "Na", y : sodium});
  mineralData.push({x : "Zn", y : zinc});
  return mineralData;
}

function ItemDetailCharts (props) {
  return (
    <div>
      <VictoryChart
        domainPadding={30}
        theme={VictoryTheme.material}
      >
        <VictoryAxis 
          dependentAxis
          label="kCal per 100g"
          style={{
            axisLabel: {padding: 35}
          }}
        />
        <VictoryAxis />
        <VictoryBar 
          data={makekCalData(props)} />
      </VictoryChart>
      <VictoryChart theme={VictoryTheme.material}>
        <VictoryBar data={makeVitaminData(props)} />
      </VictoryChart>
      <VictoryChart theme={VictoryTheme.material}>
        <VictoryScatter data={makeMineralData(props)}></VictoryScatter>
        <VictoryAxis 
          dependentAxis
          label="mcg per 100g"
          style={{
            axisLabel : {padding: 35}
          }}
        />
        <VictoryAxis />
      </VictoryChart>
    </div>
  );
}

export default ItemDetailCharts;
