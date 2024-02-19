module.exports = (sequelize, DataTypes) =>{
    return sequelize.define('feedingHabits',{
        feedingHabits_id: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
          },
        local_products: {
            type: DataTypes.BOOLEAN,
            allowNull: true
        },
        co2_emissions: {
            type: DataTypes.FLOAT,
            allowNull: true
        }
    });
}