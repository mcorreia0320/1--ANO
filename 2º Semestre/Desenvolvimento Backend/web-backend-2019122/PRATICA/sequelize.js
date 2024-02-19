const { Sequelize, DataTypes } = require('sequelize')

const UserDataModel = require('./models/User');
const RentalDataModel = require('./models/Rental');

const sequelize = new Sequelize(process.env.DB_SCHEMA, process.env.DB_USER, process.env.DB_PASS, {
    dialect: 'mysql',
    host: process.env.DB_HOST
});

const User = UserDataModel(sequelize, DataTypes);
const Rental = RentalDataModel(sequelize, DataTypes);

User.hasMany(Rental);
Rental.belongsTo(User, {foreignKey: 'user_id'});

sequelize.authenticate()
    .then(()=>{
        console.log('Connection has been established');
    })
    .catch((err)=>{
        console.error("Unable to connect", err);
    })

sequelize.sync({ force: false })
.then(()=>{
    console.log('Database & tables created!')
})

module.exports = {
    User, Rental
}