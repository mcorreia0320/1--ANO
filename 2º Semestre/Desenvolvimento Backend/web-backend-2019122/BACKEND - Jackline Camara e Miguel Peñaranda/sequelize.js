// TODO Implement all the models and business logic using sequelize
const { Sequelize, DataTypes } = require('sequelize');

const UserDataModel = require('./models/User');
const UserHomeDataModel = require('./models/UserHome');
const UserTransportDataModel = require('./models/UserTransport');
const TransportDataModel = require('./models/Transport');
const GasConsumptionDataModel = require('./models/GasConsumption');
const FeedingHabitsDataModel = require('./models/FeedingHabits');
const AccountDataModel = require('./models/Account');
const ElectricityConsumptionDataModel = require('./models/ElectricityConsumption');
const DietDataModel = require('./models/Diet');
const historialFootPrint = require('./models/HistorialFootPrint')

const sequelize = new Sequelize(process.env.DB_SCHEMA, process.env.DB_USER, process.env.DB_PASS, {
    dialect: 'mysql',
    host: process.env.DB_HOST,
    dialectOptions: {
        ssl: {
           require: false
        }
      },
    pool: {
        max: 10,
        min: 0,
        acquire: 30000,
        idle: 10000
      }
});

const User = UserDataModel(sequelize, DataTypes);
const UserHome = UserHomeDataModel(sequelize, DataTypes);
const UserTransport = UserTransportDataModel(sequelize, DataTypes);
const Transport = TransportDataModel(sequelize, DataTypes);
const GasConsumption = GasConsumptionDataModel(sequelize, DataTypes);
const FeedingHabits = FeedingHabitsDataModel(sequelize, DataTypes);
const Account = AccountDataModel(sequelize, DataTypes);
const ElectricityConsumption = ElectricityConsumptionDataModel(sequelize, DataTypes);
const Diet = DietDataModel(sequelize, DataTypes);
const Historial = historialFootPrint(sequelize, DataTypes);

// Define relationships

User.hasMany(UserHome, {onDelete: 'CASCADE'});
UserHome.belongsTo(User);

Account.hasOne(User, {onDelete: 'CASCADE'});
User.belongsTo(Account);

Account.hasOne(Historial, {onDelete: 'CASCADE'});
Historial.belongsTo(Account);

User.hasMany(UserTransport, {onDelete: 'CASCADE'});
UserTransport.belongsTo(User);

Transport.hasMany(UserTransport, {onDelete: 'CASCADE'});
UserTransport.belongsTo(Transport);

User.hasMany(FeedingHabits, {onDelete: 'CASCADE'});
FeedingHabits.belongsTo(User);

Diet.hasMany(FeedingHabits, {onDelete: 'CASCADE'});
FeedingHabits.belongsTo(Diet);

GasConsumption.hasMany(UserHome);
UserHome.belongsTo(GasConsumption);

ElectricityConsumption.hasMany(UserHome);
UserHome.belongsTo(ElectricityConsumption);


sequelize.authenticate()
    .then(()=> {
        console.log("Connection has been established")
    })
    .catch(err => {
        console.error("Unable to connect",err);
    });

sequelize.sync({ force: false })
     .then(()=>{
         console.log('Database & tables created!');
     });

// Transport.bulkCreate([
//     {type_transport: 'Ando a pé'},
//     {type_transport: 'Carro'},
//     {type_transport: 'Carro Elétrico'},
//     {type_transport: 'Mota'},
//     {type_transport: 'Mota Elétrica'},
//     {type_transport: 'Autocarro'},
//     {type_transport: 'Bicicleta'},
//     {type_transport: 'Bicicleta Elétrica'},
//     {type_transport: 'Trotinente Elétrico'}
// ])

// Diet.bulkCreate([
//     {diet_type: 'Omnivoro'},
//     {diet_type: 'Vegetarian'},
//     {diet_type: 'Vegan'}
// ])

// ElectricityConsumption.bulkCreate([
//         {monthly_consumption: 'Entre 10 e 20 euros...', co2_emissions: 24.2},
//         {monthly_consumption: 'Entre 20 e 30 euros...', co2_emissions: 40.04},
//         {monthly_consumption: 'Entre 30 e 40 euros...', co2_emissions: 56.52},
//         {monthly_consumption: 'Entre 40 e 50 euros...', co2_emissions: 72.67},
//         {monthly_consumption: 'Entre 50 e 60 euros...', co2_emissions: 88.81},
//         {monthly_consumption: 'Entre 60 e 70 euros...', co2_emissions: 104.96},
//         {monthly_consumption: 'Entre 70 e 80 euros...', co2_emissions: 121.11},
//         {monthly_consumption: 'Entre 80 e 90 euros...', co2_emissions: 137.26},
//         {monthly_consumption: 'Entre 90 e 100 euros...', co2_emissions: 153.41},
//         {monthly_consumption: 'Más de 100...', co2_emissions: 193.78}
        
// ])

// GasConsumption.bulkCreate([
//     {monthly_consumption: 'Entre 10 e 20 euros...', co2_emissions: 7.37},
//     {monthly_consumption: 'Entre 20 e 30 euros...', co2_emissions: 12.27},
//     {monthly_consumption: 'Entre 30 e 40 euros...', co2_emissions: 17.18},
//     {monthly_consumption: 'Entre 40 e 50 euros...', co2_emissions: 22.10},
//     {monthly_consumption: 'Entre 50 e 60 euros...', co2_emissions: 27.15},
//     {monthly_consumption: 'Entre 60 e 70 euros...', co2_emissions: 31.91},
//     {monthly_consumption: 'Entre 70 e 80 euros...', co2_emissions: 36.82},
//     {monthly_consumption: 'Entre 80 e 90 euros...', co2_emissions: 41.73},
//     {monthly_consumption: 'Entre 90 e 100 euros...', co2_emissions: 46.64},
//     {monthly_consumption: 'Más de 100...', co2_emissions: 58.92}
// ])

     module.exports ={
        User, UserHome, Account, UserTransport, Transport, GasConsumption, ElectricityConsumption, FeedingHabits, Diet, Historial
    }
