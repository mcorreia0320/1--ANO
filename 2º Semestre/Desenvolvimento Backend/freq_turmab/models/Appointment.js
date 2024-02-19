module.exports = (sequelize, DataTypes) =>{
    return sequelize.define('appointments',{
        appointment_id: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        appointment_datetime: {
            type: DataTypes.DATE
        },
        duration_minutes: {
            type: DataTypes.INTEGER
        }
    });
}