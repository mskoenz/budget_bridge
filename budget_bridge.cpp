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
#include <fstream>
#include <fsc/ArgParser.hpp>

int main(int argc, char * argv[]) {
    fsc::ArgParser ap(argc, argv);
    
    if(ap.is_set("v")) {
        std::cout << "0.1" << std::endl;
        return 0;
    }
    
    if(ap.is_set("param") or ap.is_set("p")) {
        std::cout << "energy" << std::endl;
        std::cout << "velocity" << std::endl;
        return 0;
    }
     
    double energy = ap["energy"];
    double velocity = ap["velocity"];
    
    if(ap.freeargc() == 2) {
        std::vector<double> a[3];
        for(uint32_t n = 0; n < 3; ++n) {
            a[n].resize(9);
        }
        
        std::string in;
        
        for(uint32_t n = 0; n < 2; ++n) {
            std::string filename = ap[n];
            std::ifstream is(filename);
            
            if(is.is_open())
                for(uint32_t i = 0; i < 9; ++i) {
                    is >> in;
                    a[n][i] = std::stoi(in);
                }
            is.close();
        }
        
        std::ofstream os("res.txt");
        for(uint32_t i = 0; i < 9; ++i) {
            a[2][i] = (a[1][i] - a[0][i])*energy - velocity;
            os << a[2][i] << "\n";
        }
        os.close();
        
        
        
        
    } else {
        std::cout << energy << std::endl;
        std::cout << velocity << std::endl;
    }
    
    
    return 0;
}
