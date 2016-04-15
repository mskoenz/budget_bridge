/** ****************************************************************************
 * \brief      
 * \file
 * \author
 * Year      | Name
 * --------: | :------------
 * 2016      | Mario S. Koenz
 * \copyright  todo
 ******************************************************************************/

#include <iostream>
#include <fsc/ArgParser.hpp>

int main(int argc, char * argv[]) {
    fsc::ArgParser ap(argc, argv);
    
    if(ap.is_set("param") or ap.is_set("p")) {
        std::cout << "energy" << std::endl;
        std::cout << "velocity" << std::endl;
        return 0;
    }
    
    double energy = ap["energy"];
    double velocity = ap["velocity"];
    
    std::cout << energy << std::endl;
    std::cout << velocity << std::endl;
    
    return 0;
}
