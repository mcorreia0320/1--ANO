const { UserHome, Historial, Diet, GasConsumption, ElectricityConsumption, Transport } = require('../sequelize');


exports.totalFootPrint = function (req, res) {
    UserHome.count().then(count =>{
        if (count != 0) {
            res.status(200).json({counter: count});
        }
        else res.status(404).json({message: 'Nobody calculated the foot print already'})
    }).catch( () => {
        res.status(500).json({message: 'Something went wrong!'})
    })
}

exports.getAllFootPrints = function (req, res) {
    Historial.findAll().then( historial =>{
        if (historial != null) {
            res.status(200).json(historial)
        } else res.status(404).json({message: 'Nobody calculated the foot print already'}) 
    }).catch( () => {
        res.status(500).json({message: 'Something went wrong!'})
    })
}

exports.getAllTransports = function (req, res) {
    Transport.findAll({attributes: ['type_transport']}).then(result =>{
        res.status(200).json(result);
    })
}

exports.getAllDiets = function (req, res) {
    Diet.findAll({attributes: ['diet_type']}).then(result =>{
        res.status(200).json(result);
    })
}

exports.getAllGasValues = function (req, res) {
    GasConsumption.findAll({attributes: ['monthly_consumption']}).then(result =>{
        res.status(200).json(result);
    })
}

exports.getAllElectricityValues = function (req, res) {
    ElectricityConsumption.findAll({attributes: ['monthly_consumption']}).then(result =>{
        res.status(200).json(result);
    })
}