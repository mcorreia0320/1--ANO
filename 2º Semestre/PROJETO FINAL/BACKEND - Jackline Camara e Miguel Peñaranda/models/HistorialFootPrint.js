module.exports = (sequelize, DataTypes) =>{
    return sequelize.define('historialFootPrint',{
        historial_id: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
          },
        totalEmissions: {
            type: DataTypes.FLOAT
        }
    });
}