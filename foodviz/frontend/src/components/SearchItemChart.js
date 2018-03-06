import React from 'react';
import ItemDetailCharts from './ItemDetailCharts';
import { Modal, ModalHeader, ModalBody } from 'reactstrap';
import { VictoryChart, VictoryBar } from 'victory';
import '../styles/SearchItemChart.css';

class SearchItemChart extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      modal: false,
    }
    this.toggle = this.toggle.bind(this)
  }

  toggle() {
    this.setState({
      modal: !this.state.modal
    });
  }

  makeData() {
    const chartData = [];
    const protein = this.props.data["protein"];
    const carbohydrates = this.props.data["carbohydrates"];
    const fat = this.props.data["fat"];
    const sugar = this.props.data["sugar"];
    const fiber = this.props.data["fiber"];
    chartData.push({x: "protein", y : protein});
    chartData.push({x: "carbohydrates", y : carbohydrates});
    chartData.push({x: "fat", y : fat});
    chartData.push({x: "sugar", y : sugar});
    chartData.push({x: "fiber", y : fiber});
    return chartData;
  }

  render (){
    return (
      <div 
        onClick={this.toggle}
        className="modal-button">
        <VictoryChart
         domainPadding={20}>
         <VictoryBar 
           data={this.makeData()}
         />
        </VictoryChart>
        <Modal isOpen={this.state.modal}>
          <ModalHeader toggle={this.toggle}>{this.props.data["description"]}</ModalHeader>
          <ModalBody>
            <ItemDetailCharts data={this.props.data} />
          </ModalBody>
        </Modal>
      </div>
    );
  }
}

export default SearchItemChart;
