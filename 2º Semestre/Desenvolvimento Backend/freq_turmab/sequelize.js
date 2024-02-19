const { Sequelize, DataTypes } = require('sequelize');

const AppointmentsDataModel = require('./models/Appointment');
const DentistDataModel = require('./models/Dentist');
const PatientDataModel = require('./models/Patient');

const sequelize = new Sequelize(process.env.DB_SCHEMA, process.env.DB_USER, process.env.DB_PASS, {
    dialect: 'mysql',
    host: process.env.DB_HOST
});

const Dentist = DentistDataModel(sequelize, DataTypes);
const Patient = PatientDataModel(sequelize, DataTypes);
const Appointment = AppointmentsDataModel(sequelize, DataTypes);

Patient.hasMany(Appointment);
Appointment.belongsTo(Patient, {foreignKey: 'patient_id'});

Dentist.hasMany(Appointment);
Appointment.belongsTo(Dentist, {foreignKey: 'dentist_id'});

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

// Patient.bulkCreate([
//     {first_name: 'Miguel', last_name: 'Correia', email: 'miguel@gmail.com'},
//     {first_name: 'Saul', last_name: 'Pinto', email: 'saul@gmail.com'},
//     {first_name: 'Jacky', last_name: 'Camara', email: 'jacky@gmail.com'}
// ])

// Dentist.bulkCreate([
//     {first_name: 'David', last_name: 'Jardim', email: 'david@gmail.com'},
//     {first_name: 'Fabio', last_name: 'Camacho', email: 'fabio@gmail.com'},
//     {first_name: 'Mango', last_name: 'Andrade', email: 'magno@gmail.com'}
// ])

// Appointment.bulkCreate([
//     {dentist_id: 1, patient_id: 3, appointment_datetime: '2023-06-21', duration_minutes: 30},
//     {dentist_id: 2, patient_id: 2, appointment_datetime: '2023-03-15', duration_minutes: 60},
//     {dentist_id: 3, patient_id: 1, appointment_datetime: '2023-10-30', duration_minutes: 20},
// ])

module.exports ={
    Appointment, Dentist, Patient
}
