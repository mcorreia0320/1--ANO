module.exports = (sequelize, DataTypes) =>{
    return sequelize.define('grades',{
        grade_id: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
          },
        grade: {
            type: DataTypes.DECIMAL
        }
    });
}