import React, { Component } from 'react';
import { Link } from "react-router-dom";
import axios from 'axios';
import Calendar from 'react-calendar';
import DatePicker from 'react-datepicker';
import Iframe from 'react-iframe';
import ReactList from 'react-list';
import Select from 'react-select';
import Button from 'react';
import Moment from 'moment';
import ScrollBox from 'react-scroll-box';
import ScrollAxes from 'react-scroll-box';
import FastTrack from 'react-scroll-box';

import 'react-calendar/dist/Calendar.css';
import 'react-datepicker/dist/react-datepicker.css';



const cameraEx = [
    {
        value: 'camera1',
        label: 'camera1'
    },
    {
        value: 'camera2',
        label: 'camera2',
    },
    {
        value: 'camera3',
        label: 'camera3',
    },
    {
        value: 'camera4',
        label: 'camera4'
    },
];

const options = [
    { value: 'chocolate', label: 'Chocolate' },
    { value: 'strawberry', label: 'Strawberry' },
    { value: 'vanilla', label: 'Vanilla' },
  ];


const noFootage = {
    camera: "No Footage Found",
    url: "https://lh3.googleusercontent.com/proxy/ti14ZWpDmziFp4qmZ535eT7VZchOWdTYaZzDQ2zFXT74R8KBcg5GABh9Mqj8xrBk9RzSkvCoISfhww"
} 
export default class MainPage extends Component {
    constructor(props) {
        super(props);

        this.onChangeDate = this.onChangeDate.bind(this);
        this.renderCamera = this.renderCamera.bind(this);
        this.onClickFootage = this.onClickFootage.bind(this);
        this.onSelectCamera = this.onSelectCamera.bind(this);
        this.updateAccessList = this.updateAccessList.bind(this);
        this.renderAccesses = this.renderAccesses.bind(this);
        //this.updateFootage = this.updateFootage.bind(this);

        this.state = {
            selectedDate: new Date(),
            cameraList: [{}],
            footageList: [],
            selectedFootage: {},
            selectedCamera: {},
            accessList: [],
        }
    }

    // Call backend here
    componentDidMount() {
        axios.get('http://localhost:8000/CameraList')
            .then(response => {
                this.setState({
                    selectedDate: Date.now(),
                    selectedTimeUrl: '',
                });
                let tempList = []
                response.data.forEach(function(camera){
                    tempList.push({
                        value: camera.id,
                        label: camera.coordinates
                    })
                });
                this.setState({
                    cameraList: tempList
                })
                console.log(`cameraList:`, this.state.cameraList);
                if(this.state.cameraList.length > 0)
                {
                    this.setState({
                        selectedCamera: this.state.cameraList[0]
                    })
                }
                else 
                {
                    console.log(`No camera available`)
                    this.setState({
                        selectedCamera: null
                    })
                }
                console.log(`initialized camera: `, this.state.selectedCamera)
                this.updateFootage();
            })
            .catch((error) => {
                console.log(error);
            })
    }

    updateAccessList(cameraId) {
        axios.get('http://localhost:8000/AccessList/camera/' + cameraId)
                .then(response => {
                    console.log(`data is: `, response.data)
                    let stringList = [];
                    let string = "";
                    response.data.forEach(function(accessObject){
                        string = string + accessObject.username;
                        string = string + " accessed footage: (";
                        string = string + accessObject.accessed_footage_date;
                        string = string + ", " + accessObject.accessed_footage_time;
                        string = string + ") on (" + accessObject.date + " at " + accessObject.time + ")";
                        stringList.push(string);
                        string = "";
                    })
                    this.setState({
                        accessList: stringList
                    })
                    console.log(`stringList: `, this.state.accessList);
                })
                .catch((error) => {
                    console.log(error);
                })
    }

    updateFootage = () => {
        console.log(`Camera selected:`, this.state.selectedCamera)
        if(this.state.selectedCamera != null)
        {
            let filter = {
                id: this.state.selectedCamera.value,
                date: this.state.selectedDate
            }
            console.log(`footage filter by:`, filter);
            axios.get('http://localhost:8000/FootageList/camera/' + filter.id + '/date/' + Moment(filter.date).format('YYYY-MM-DD'))
                .then(response => {
                    let tempList = []
                    response.data.forEach(function(footage){
                        tempList.push({
                            id: footage.id,
                            camera: footage.camera,
                            date: footage.date,
                            time: footage.time,
                            url: footage.URL
                        })
                    })
                    this.setState({
                        footageList: tempList
                    },
                    console.log(`footage list: `, tempList));
                    if(this.state.footageList.length > 0)
                    {
                        this.setState({
                            selectedFootage: this.state.footageList[0]
                        })
                    }
                    else
                    {
                        this.setState({
                            selectedFootage: noFootage
                        })
                    }
                    this.updateAccessList(filter.id);
                })
                .catch((error) => {
                    console.log(error);
                })
        }
        else
        {
            this.setState({
                footageList: []
            })
        }
    }

    onChangeDate(date) {
        this.setState({
            selectedDate: date
        },
        this.updateFootage
        );
    }

    onSelectCamera(camera) {
        this.setState(
        { 
            selectedCamera: camera
        },
        this.updateFootage
        );
    }

    addAccessInstance = () => {
        let req = {
            username: "Take",
            accessed_camera: this.state.selectedFootage.camera,
            accessed_footage: this.state.selectedFootage.id
        }
        console.log(`posting access instance: `, req)
        axios.post('http://127.0.0.1:8000/AccessList/camera/' + this.state.selectedFootage.camera, req)
        .then (response => {
            console.log(`reaccesing access instances`)
            this.updateAccessList(this.state.selectedCamera.value)
        })
        .catch((error) => {
            console.log(error);
        })
    }

    onClickFootage(footage) {
        console.log(`Footage selected: `, footage);
        this.setState({
            selectedFootage: footage
        },
        this.addAccessInstance
        );
    }

    renderCamera(index, key) {
        console.log(`footageList render camera: `, this.state.footageList);
        if (this.state.footageList.length > 1)
        {
            return  <div style = {cameraList}>
                        <button style = {{width: "95%"}}
                            key={key} onClick={() => this.onClickFootage(this.state.footageList[index])}> {this.state.footageList[index].time}

                        </button>
                        
                    </div>
        }
        else if(this.state.footageList.length === 1)
        {
            if(this.state.footageList[0] === {})
            {
                return  <div style = {cameraList}>
                            <h6>No Footage</h6>
                        </div>
            }
            else
            {
                return  <div style = {cameraList}>
                            <button style = {{width: "95%"}}
                                onClick={() => this.onClickFootage(this.state.footageList[0])}> {this.state.footageList[0].time}
                            </button>     
                        </div>
            }
        }
        else
        {
            console.log(`No Footage Available`);
            return  <div>
                        <h6>No Footage</h6>
                    </div>
        }
    }

    renderAccesses(index, key) {
        const listItems = this.state.accessList.map((str) => <li key={str}>{str}</li>)
        console.log(`accessList: `, this.state.accessList);
        if (this.state.accessList.length > 0)
        {
            return listItems
        }
        else if(this.state.accessList.length === 1)
        {
            return  <li>
                        {this.state.accessList[0]}    
                    </li>
                   
        }
        else
        {
            return <li>No audit logs available for this camera</li>
        }
    }
        
    render() {
        const header = "Camera: " + this.state.selectedCamera.label + "  Date: " 
        + Moment(this.state.selectedDate).format('YYYY-MM-DD') + " Footage: " 
        + this.state.selectedFootage.time;
        return (
            <div>
                <div style = {divstyle1}> 
                    <h3>Select Footage Date</h3>
                    <DatePicker
                        defaultValue = {Date.now()}
                        selected = {this.state.selectedDate}
                        onChange = {this.onChangeDate}
                    />
                    <h3>Select Camera</h3>
                    <Select
                        value={this.state.selectedCamera}
                        onChange={this.onSelectCamera}
                        options={this.state.cameraList}
                    />
                    <h4>Select Footage</h4>
                    <div style = {scrollList}>
                        <ReactList
                            length = {this.state.footageList.length}
                            type = 'uniform'
                            itemRenderer = {this.renderCamera}
                        />
                    </div>
                </div>
                <div style = {divstyle2}>
                    <h6>{header}</h6>
                    <Iframe
                        url={this.state.selectedFootage.url}
                        width="800px"
                        height="770px"
                        position="relative"
                    />
                </div>
                <div style = {divstyle3}>
                    {this.renderAccesses()}
                </div>
            </div>
        )
    }
}

var cameraList = {
    padding: "10px",
    fontSize: "15px"
}

var scrollList = {
    padding: "10px",
    marginTop: "5%",
    border:'1px solid black',
    height: "600px",
    fontSize: "16px"
}

var divstyle1 = {
    float: "left",
    padding: "20px",
    marginLeft: "0%",
    marginTop: "0%",
    width: "250px"
}

var divstyle2 = {
    float: "left",
    padding: "2px",
    marginLeft: "2%",
    marginTop: "2%",
    width: "550px"
}

var divstyle3 = {
    float: "left",
    padding: "2px",
    marginLeft: "15%",
    marginTop: "4%",
    width: "700px",
    height: "760px",
    overflowY: 'scroll',
    border:'1px solid black', 
};