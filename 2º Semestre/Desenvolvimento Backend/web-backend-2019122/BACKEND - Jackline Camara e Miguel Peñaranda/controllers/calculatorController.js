const { FeedingHabits, UserTransport, UserHome, Historial  } = require('../sequelize');

// Preencher formulario dos habits alimenticios por primera vez

exports.fillHabits = function (req, res) {
   var { localProducts, typeDiet } = req.body;
   var co2Emissions = 0;
   var id = req.headers['user-id'];

   if ( localProducts == 'Sim') {
        localProducts = 1;
        co2Emissions += 0.2
   } else {localProducts = 0; co2Emissions += 0.5}

   if (typeDiet == 'Omnivoro') {
        typeDiet = 1;
        co2Emissions += 208;
   }
   else if  (typeDiet == 'Vegetarian') {
        typeDiet = 2;
        co2Emissions += 142;
   }
   else { typeDiet = 3; co2Emissions += 125;}

   FeedingHabits.create({'local_products': localProducts, 'co2_emissions': co2Emissions, 'userUserId': id, 'dietDietId': typeDiet })
   .then(() => {
        res.status(200).json({message: 'Habitos Alimenticios preenchidos com successo'});
   }).catch(err =>{
        res.status(400).json(err);
   })
}

// Preencher formulario dos habits alimenticios caso não seja a primera vez, apenas atualiza os ultimos dados

exports.updateHabits = function (req, res) {
    var { localProducts, typeDiet } = req.body;
    var co2Emissions = 0;
    var id = req.headers['user-id'];
 
    if ( localProducts == 'Sim') {
         localProducts = 1;
         co2Emissions += 0.2
    } else {localProducts = 0; co2Emissions += 0.5}
 
    if (typeDiet == 'Omnivoro') {
         typeDiet = 1; 
         co2Emissions += 208;
    }
    else if  (typeDiet == 'Vegetarian') {
         typeDiet = 2;
         co2Emissions += 142;
    }
    else {typeDiet = 3; co2Emissions += 125;}
 
    FeedingHabits.update({'local_products': localProducts, 'co2_emissions': co2Emissions, 'dietDietId': typeDiet }, {where: {userUserId: id}})
    .then(() => {
         res.status(200).json({message: 'Habitos Alimenticios atualizados com successo'});
    }).catch(err =>{
         res.status(400).json(err);
    })
 }

 // Preencher formulario da Informação do Hogar por primera vez

exports.fillInfoHome = function(req,res) {
     var {amountPeople, sizeHome, recycling, consumptionsGas, consumptionsElectricity } = req.body;
     var co2Emissions = 0;
     var id = req.headers['user-id'];

     co2Emissions += sizeHome * 4.20; // Emission por metro^2

     FeedingHabits.findOne({where: {'userUserId': id }}).then(habitUser =>{  // Emission por Habitos
          co2Emissions += habitUser.co2_emissions;
     })

     UserTransport.findOne({where: {'userUserId': id}}).then(userTransport =>{ // Emission por Transporte
          co2Emissions += userTransport.CO2_emissions;
     })

     // Condições para a opçao escolhida do consumo de gas no front-end 

     if (consumptionsGas == 'Entre 10 e 20 euros...') {
          consumptionsGas = 1;
          co2Emissions += 7.37;
     }
     else if (consumptionsGas == 'Entre 20 e 30 euros...') {
          consumptionsGas = 2;
          co2Emissions += 12.27;
     }
     else if (consumptionsGas == 'Entre 30 e 40 euros...') {
          consumptionsGas = 3;
          co2Emissions += 17.18;
     }
     else if (consumptionsGas == 'Entre 40 e 50 euros...') {
          consumptionsGas = 4;
          co2Emissions += 22.10;
     }
     else if (consumptionsGas == 'Entre 50 e 60 euros...') {
          consumptionsGas = 5;
          co2Emissions += 27.15;
     }
     else if (consumptionsGas == 'Entre 60 e 70 euros...') {
          consumptionsGas = 6;
          co2Emissions += 31.91;
     }
     else if (consumptionsGas == 'Entre 70 e 80 euros...') {
          consumptionsGas = 7;
          co2Emissions += 36.82;
     }
     else if (consumptionsGas == 'Entre 80 e 90 euros...') {
          consumptionsGas = 8;
          co2Emissions += 41.73;
     }
     else if (consumptionsGas == 'Entre 90 e 100 euros...') {
          consumptionsGas = 9;
          co2Emissions += 46.64;
     } else {consumptionsGas = 10; co2Emissions += 58.92}

     // Condições para a opçao escolhida do consumo de electricidade no front-end 

     if (consumptionsElectricity == 'Entre 10 e 20 euros...') {
          consumptionsElectricity = 1;
          co2Emissions += 24.2;
     }
     else if (consumptionsElectricity == 'Entre 20 e 30 euros...') {
          consumptionsElectricity = 2;
          co2Emissions += 40.04;
     }
     else if (consumptionsElectricity == 'Entre 30 e 40 euros...') {
          consumptionsElectricity = 3;
          co2Emissions += 56.52;
     }
     else if (consumptionsElectricity == 'Entre 40 e 50 euros...') {
          consumptionsElectricity = 4;
          co2Emissions += 72.67;
     }
     else if (consumptionsElectricity == 'Entre 50 e 60 euros...') {
          consumptionsElectricity = 5;
          co2Emissions += 88.81;
     }
     else if (consumptionsElectricity == 'Entre 60 e 70 euros...') {
          consumptionsElectricity = 6;
          co2Emissions += 104.96;
     }
     else if (consumptionsElectricity == 'Entre 70 e 80 euros...') {
          consumptionsElectricity = 7;
          co2Emissions += 121.11;
     }
     else if (consumptionsElectricity == 'Entre 80 e 90 euros...') {
          consumptionsElectricity = 8;
          co2Emissions += 137.26;
     }
     else if (consumptionsElectricity == 'Entre 90 e 100 euros...') {
          consumptionsElectricity = 9;
          co2Emissions += 153.41;
     } else {consumptionsElectricity = 10; co2Emissions += 193.78}

     if (recycling == 'Sim') {
          recycling = 1;
          co2Emissions -= 2.5 // Caso a pessoa recicle é feito um desconto
     } else recycling = 0;

     co2Emissions = co2Emissions / amountPeople;

     UserHome.create({'amount_people': amountPeople, 'size': sizeHome, 'recycling': recycling, 'total_co2_emissions': co2Emissions, 'userUserId': id, 'gasConsumptionGasConsumptionId': consumptionsGas, 'electricityConsumptionElectricityConsumptionId': consumptionsElectricity})
     .then(() => {
          res.status(200).json({message: 'Informação do hogar preenchidos com successo'});
     }).catch(err =>{
          res.status(400).json(err);
     })

     Historial.create({'totalEmissions': co2Emissions, 'accountAccountId': id});
}

// Preencher formulario da informação do hogar caso não seja a primera vez, apenas atualiza os ultimos dados

exports.UpdateInfoHome = function(req,res) {
     var {amountPeople, sizeHome, recycling, consumptionsGas, consumptionsElectricity } = req.body;
     var co2Emissions = 0;
     var id = req.headers['user-id'];

     co2Emissions += sizeHome * 4.20; // Emission por metro^2

     FeedingHabits.findOne({where: {'userUserId': id }}).then(habitUser =>{  // Emission por Habitos
          co2Emissions += habitUser.co2_emissions;
     })

     UserTransport.findOne({where: {'userUserId': id}}).then(userTransport =>{ // Emission por Transporte
          co2Emissions += userTransport.CO2_emissions;
     })

     // Condições para a opçao escolhida do consumo de gas no front-end 

     if (consumptionsGas == 'Entre 10 e 20 euros...') {
          consumptionsGas = 1;
          co2Emissions += 7.37;
     }
     else if (consumptionsGas == 'Entre 20 e 30 euros...') {
          consumptionsGas = 2;
          co2Emissions += 12.27;
     }
     else if (consumptionsGas == 'Entre 30 e 40 euros...') {
          consumptionsGas = 3;
          co2Emissions += 17.18;
     }
     else if (consumptionsGas == 'Entre 40 e 50 euros...') {
          consumptionsGas = 4;
          co2Emissions += 22.10;
     }
     else if (consumptionsGas == 'Entre 50 e 60 euros...') {
          consumptionsGas = 5;
          co2Emissions += 27.15;
     }
     else if (consumptionsGas == 'Entre 60 e 70 euros...') {
          consumptionsGas = 6;
          co2Emissions += 31.91;
     }
     else if (consumptionsGas == 'Entre 70 e 80 euros...') {
          consumptionsGas = 7;
          co2Emissions += 36.82;
     }
     else if (consumptionsGas == 'Entre 80 e 90 euros...') {
          consumptionsGas = 8;
          co2Emissions += 41.73;
     }
     else if (consumptionsGas == 'Entre 90 e 100 euros...') {
          consumptionsGas = 9;
          co2Emissions += 46.64;
     } else {consumptionsGas = 10; co2Emissions += 58.92}

     // Condições para a opçao escolhida do consumo de electricidade no front-end 

     if (consumptionsElectricity == 'Entre 10 e 20 euros...') {
          consumptionsElectricity = 1;
          co2Emissions += 24.2;
     }
     else if (consumptionsElectricity == 'Entre 20 e 30 euros...') {
          consumptionsElectricity = 2;
          co2Emissions += 40.04;
     }
     else if (consumptionsElectricity == 'Entre 30 e 40 euros...') {
          consumptionsElectricity = 3;
          co2Emissions += 56.52;
     }
     else if (consumptionsElectricity == 'Entre 40 e 50 euros...') {
          consumptionsElectricity = 4;
          co2Emissions += 72.67;
     }
     else if (consumptionsElectricity == 'Entre 50 e 60 euros...') {
          consumptionsElectricity = 5;
          co2Emissions += 88.81;
     }
     else if (consumptionsElectricity == 'Entre 60 e 70 euros...') {
          consumptionsElectricity = 6;
          co2Emissions += 104.96;
     }
     else if (consumptionsElectricity == 'Entre 70 e 80 euros...') {
          consumptionsElectricity = 7;
          co2Emissions += 121.11;
     }
     else if (consumptionsElectricity == 'Entre 80 e 90 euros...') {
          consumptionsElectricity = 8;
          co2Emissions += 137.26;
     }
     else if (consumptionsElectricity == 'Entre 90 e 100 euros...') {
          consumptionsElectricity = 9;
          co2Emissions += 153.41;
     } else {consumptionsElectricity = 10; co2Emissions += 193.78}

     if (recycling == 'Sim') {
          recycling = 1;
          co2Emissions -= 2.5 // Caso a pessoa recicle é feito um desconto
     } else recycling = 0;

     co2Emissions = co2Emissions / amountPeople;

     UserHome.update({'amount_people': amountPeople, 'size': sizeHome, 'recycling': recycling, 'total_co2_emissions': co2Emissions, 'gasConsumptionGasConsumptionId': consumptionsGas, 'electricityConsumptionElectricityConsumptionId': consumptionsElectricity}, {where: {'userUserId': id}})
     .then(() => {
          res.status(200).json({message: 'Informação do hogar atualizados com successo'});
     }).catch(err =>{
          res.status(400).json(err);
     })

     Historial.create({'totalEmissions': co2Emissions, 'accountAccountId': id});
}

// Preencher formulario dos Habitos de Transporte por primera vez

exports.fillHabitsTransport = function(req,res) {
     var id = req.headers['user-id'];
     var {distanceTraveled, typeTransport} = req.body;
     var co2Emissions = 0;

     if (typeTransport == 'Ando a pé') {
          typeTransport = 1;
     }
     else if (typeTransport == 'Carro') {
          typeTransport = 2;
          co2Emissions = distanceTraveled * 0.137;
     }
     else if (typeTransport == 'Carro Elétrico') {
          typeTransport = 3;
          co2Emissions = distanceTraveled * 0.05;
     }
     else if (typeTransport == 'Mota') {
          typeTransport = 4;
          co2Emissions = distanceTraveled * 0.1;
     }
     else if (typeTransport == 'Mota Elétrica') {
          typeTransport = 5;
          co2Emissions = distanceTraveled * 0.02;
     }
     else if (typeTransport == 'Autocarro') {
          typeTransport = 6;
          co2Emissions = distanceTraveled * 0.07;
     }
     else if (typeTransport == 'Bicicleta') {
          typeTransport = 7;
     }
     else if (typeTransport == 'Bicicleta Elétrica') {
          typeTransport = 8;
          co2Emissions = distanceTraveled * 0.015;
     }
     else {typeTransport = 9; co2Emissions = distanceTraveled * 0.02}

     UserTransport.create({'distance_traveled': distanceTraveled, 'CO2_emissions': co2Emissions, 'userUserId': id, 'transportTransportId': typeTransport})
     .then(() => {
          res.status(200).json({message: 'Habitos de Transporte preenchidos com successo'});
     }).catch(err =>{
          res.status(400).json(err);
     })
}

// Preencher formulario dos Habitos de Transporte caso não seja a primera vez, apenas atualiza os ultimos dados

exports.UpdateHabitsTransport = function(req,res) {
     var id = req.headers['user-id'];
     var {distanceTraveled, typeTransport} = req.body;
     var co2Emissions = 0;

     if (typeTransport == 'Ando a pé') {
          typeTransport = 1;
     }
     else if (typeTransport == 'Carro') {
          typeTransport = 2;
          co2Emissions = distanceTraveled * 0.137;
     }
     else if (typeTransport == 'Carro Elétrico') {
          typeTransport = 3;
          co2Emissions = distanceTraveled * 0.05;
     }
     else if (typeTransport == 'Mota') {
          typeTransport = 4;
          co2Emissions = distanceTraveled * 0.1;
     }
     else if (typeTransport == 'Mota Elétrica') {
          typeTransport = 5;
          co2Emissions = distanceTraveled * 0.02;
     }
     else if (typeTransport == 'Autocarro') {
          typeTransport = 6;
          co2Emissions = distanceTraveled * 0.07;
     }
     else if (typeTransport == 'Bicicleta') {
          typeTransport = 7;
     }
     else if (typeTransport == 'Bicicleta Elétrica') {
          typeTransport = 8;
          co2Emissions = distanceTraveled * 0.015;
     }
     else {typeTransport = 9; co2Emissions = distanceTraveled * 0.02}

     UserTransport.update({'distance_traveled': distanceTraveled, 'CO2_emissions': co2Emissions, 'transportTransportId': typeTransport}, {where:{'userUserId': id}})
     .then(() => {
          res.status(200).json({message: 'Habitos de Transporte atualizados com successo'});
     }).catch(err =>{
          res.status(400).json(err);
     })
}