public int countSquare ( boolean[][] ver , boolean[][] hor ) {
    if ( ver == null || hor == null || ver.length == 0 || ver[0].length == 0 || hor.length == 0 || hor[0].length == 0 ){.1point3acres缃�
        return 0;
    }
    int[][] dpV = new int[ ver.length ][ ver[0].length ];
    int[][] dpH = new int[ hor.length ][ hor[0].length ];
    int res = 0;
    for ( int j = 0; j < dpV[0].length; ++j  ) {
        for ( int i = 0; i < dpV.length; ++i ) {
            if ( ver[j] ) {
                dpV[j] = i == 0 ? 1 : (dpV[i - 1][j] + 1);
            } else {
                dpV[j] = 0;
            }
        }
    }
    for ( int i = 0; i < dpH.length; ++i  ) {
        for ( int j = 0; j < dpH[0].length; ++j ) {
            if ( hor[j] ) {
                dpH[j] = j == 0 ? 1 : (dpH[j - 1] + 1);
            } else {
                dpH[j] = 0;
            }
        }
    }

    for ( int i = 0; i < dpH.length; ++i ) {
        for ( int j = 0; j < dpH[0].length; ++j ) {-google 1point3acres
            for ( int l = 1; l <= Math.min(dpH[0].length - j , dpV.length - i ) ; ++l  ){
                if ( dpH[ l + j - 1 ] >= l && dpH[i + l][ l + j - 1 ] >= l && dpV[i + l - 1][j ] >= l && dpV[ i + l - 1 ][ l + j ] >= l ) {
                        ++res;
                }
                if ( !(dpH[ l + j - 1 ] >= l) ) {
                    break;
                }
             }. 1point3acres.com/bbs
        }
    }
    return res; .鐣欏璁哄潧-涓€浜�-涓夊垎鍦�
}
